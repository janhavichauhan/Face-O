from importlib import resources
from pathlib import Path


def resource_filename(package_or_requirement, resource_name):
    package = resources.files(package_or_requirement)
    return str(Path(package / resource_name))