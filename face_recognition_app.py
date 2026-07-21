from pathlib import Path

import cv2
import face_recognition
import keyboard

BASE_DIR = Path(__file__).resolve().parent
KNOWN_FACES_DIR = BASE_DIR / "known_faces"
CAMERA_INDEX = 0
MATCH_TOLERANCE = 0.5


def load_known_faces(folder: Path):
    encodings = []
    names = []

    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)

    for image_path in sorted(folder.iterdir()):
        if image_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue

        image = face_recognition.load_image_file(str(image_path))
        image_encodings = face_recognition.face_encodings(image)

        if not image_encodings:
            print(f"Skipping {image_path.name}: no face found")
            continue

        encodings.append(image_encodings[0])
        names.append(image_path.stem)

    return encodings, names


def set_controls(detected: bool):
    if detected:
        keyboard.release("left")
        keyboard.press("right")
    else:
        keyboard.release("right")
        keyboard.press("left")


def main():
    known_face_encodings, known_face_names = load_known_faces(KNOWN_FACES_DIR)

    if not known_face_encodings:
        print("No usable faces found in known_faces. Add one image per person and run again.")

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError("Could not open the camera. Check camera permissions and index.")

    print("Starting Face Recognition... Press 'q' in the window to quit.")

    last_state = None

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read from camera.")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb)
            face_encodings = face_recognition.face_encodings(rgb, face_locations)

            detected = False

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                name = "Unknown"

                if known_face_encodings:
                    matches = face_recognition.compare_faces(
                        known_face_encodings,
                        face_encoding,
                        tolerance=MATCH_TOLERANCE,
                    )

                    if True in matches:
                        match_index = matches.index(True)
                        name = known_face_names[match_index]
                        detected = True

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    name,
                    (left, max(30, top - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )

            if detected != last_state:
                set_controls(detected)
                last_state = detected

            if detected:
                cv2.putText(
                    frame,
                    "Authorized",
                    (40, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    3,
                )
            else:
                cv2.putText(
                    frame,
                    "Unknown Person",
                    (40, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3,
                )

            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        keyboard.release("left")
        keyboard.release("right")


if __name__ == "__main__":
    main()
