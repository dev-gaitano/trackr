import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def save_json(filename, data):
    """Save data as JSON to data/<filename>.

    Raises:
        TypeError: if data is not JSON-serializable.
        OSError: if the file cannot be written.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    except TypeError as e:
        raise TypeError(f"Data for '{filename}' is not JSON-serializable: {e}")
    except OSError as e:
        raise OSError(f"Could not write to '{path}': {e}")


def load_json(filename):
    """Load and return JSON data from data/<filename>.

    Returns an empty list if the file does not exist or is empty.

    Raises:
        ValueError: if the file contains invalid JSON.
        OSError: if the file cannot be read.
    """
    path = os.path.join(DATA_DIR, filename)

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            content = f.read().strip()
    except OSError as e:
        raise OSError(f"Could not read from '{path}': {e}")

    if not content:
        return []

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in '{path}': {e}")
