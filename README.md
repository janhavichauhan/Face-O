# 🎯 Face Recognition Controller

A real-time **Face Recognition Controller** built using **Python**, **OpenCV**, and the **face_recognition** library. The application identifies authorized users through a webcam and performs automated actions based on recognition results.

This project demonstrates practical applications of **Computer Vision**, **Artificial Intelligence**, and **Automation**, making it suitable for security systems, smart attendance, access control, and workforce management.

---

# 📌 Features

* 📷 Real-time webcam face detection
* 🧠 AI-powered face recognition
* 👤 Recognizes multiple registered users
* 🚫 Detects unknown individuals
* ⌨️ Performs keyboard actions based on recognition
* 🟢 Displays live authorization status
* 🖼️ Draws bounding boxes and labels around detected faces
* ⚡ Lightweight and runs completely offline after setup

---

# 🛠️ Tech Stack

* Python
* OpenCV
* face_recognition
* dlib
* Keyboard
* Pathlib

---

# 📂 Project Structure

```text
Face-Recognition-Controller/
│
├── known_faces/
│   ├── Alice.jpg
│   ├── Rahul.jpg
│   └── John.png
│
├── face_recognition_app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Face-Recognition-Controller.git
cd Face-Recognition-Controller
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# 📸 Register Known Faces

Create a folder named:

```text
known_faces
```

Add one clear front-facing image for each person.

Example:

```text
known_faces/
│
├── Rahul.jpg
├── Priya.jpg
└── Alice.png
```

> **Important:** The filename becomes the person's identity displayed by the application.

---

# ▶️ Run the Application

```bash
python face_recognition_app.py
```

The webcam will open automatically.

Press **Q** to close the application.

---

# 🔄 Application Workflow

```text
Start Application
        │
        ▼
Load Registered Faces
        │
        ▼
Open Webcam
        │
        ▼
Detect Face
        │
        ▼
Generate Face Encoding
        │
        ▼
Compare with Stored Encodings
        │
        ▼
 ┌───────────────┐
 │ Face Matched? │
 └──────┬────────┘
        │
   Yes  │  No
        │
        ▼
Authorized        Unknown Person
        │
        ▼
Keyboard Action
        │
        ▼
Display Live Result
```

---

# 🧠 How Face Recognition Works

The application follows four main steps:

### 1. Face Detection

The webcam captures video frames and detects faces.

---

### 2. Face Encoding

Each detected face is converted into a unique numerical feature vector (embedding).

Example:

```text
[0.23, -0.42, 0.17, ..., 0.61]
```

This embedding represents the facial features rather than storing or comparing raw images.

---

### 3. Face Comparison

The generated embedding is compared against the embeddings stored for registered users.

If the similarity score exceeds the configured threshold (`MATCH_TOLERANCE`), the face is considered a match.

---

### 4. Action Execution

If a known face is recognized:

* Right keyboard key is pressed.
* Left key is released.
* User is marked as **Authorized**.

If the face is unknown:

* Left keyboard key is pressed.
* Right key is released.
* User is marked as **Unknown Person**.

---

# 🖥️ Sample Console Output

### Application Start

```text
Starting Face Recognition...
Press 'q' in the window to quit.
```

### Known Person

```text
Face Detected
Identity : Rahul
Status   : Authorized
```

### Unknown Person

```text
Face Detected
Identity : Unknown
Status   : Access Denied
```

---

# 📷 Expected Application Output

### Authorized User

```text
+-----------------------------------------+
|                                         |
|     [ Webcam Feed ]                     |
|                                         |
|     +---------------+                   |
|     |     Rahul     |                   |
|     +---------------+                   |
|                                         |
|     Status : Authorized                 |
|                                         |
+-----------------------------------------+
```

### Unknown User

```text
+-----------------------------------------+
|                                         |
|     [ Webcam Feed ]                     |
|                                         |
|     +---------------+                   |
|     |   Unknown     |                   |
|     +---------------+                   |
|                                         |
|     Status : Unknown Person             |
|                                         |
+-----------------------------------------+
```

---

# 📈 Proof of Functionality

The application successfully demonstrates:

* ✅ Real-time face detection using a webcam.
* ✅ Accurate face recognition of registered users.
* ✅ Identification and labeling of unknown individuals.
* ✅ Automatic keyboard event triggering based on recognition status.
* ✅ Live visualization with bounding boxes and identity labels.
* ✅ Stable continuous recognition until the user exits the application.

---

# 🔮 Future Improvements

* Employee attendance management
* Face-based login system
* Access control for restricted areas
* Multi-camera support
* Azure SQL integration
* REST API with FastAPI
* React or Streamlit dashboard
* Face recognition history logs
* Anti-spoofing (photo/video attack detection)
* Email or SMS alerts for unknown visitors

---

# 📄 License

This project is intended for educational and research purposes. Ensure that any deployment complies with applicable privacy, biometric data protection, and organizational security policies.

---

# 👨‍💻 Author

Developed using **Python**, **OpenCV**, and **face_recognition** to demonstrate practical applications of **Artificial Intelligence**, **Computer Vision**, and **Automation**.

<img width="1920" height="1080" alt="Screenshot (382)" src="https://github.com/user-attachments/assets/e4239361-b05f-4fd0-9337-a76c53a42d66" />

