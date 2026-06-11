import json
import os

DATA_DIR = "data"


def save_json(filename, data):
    """Save data as a JSON file inside the data folder."""

    # Make sure the data folder exists before writing to it
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    path = os.path.join(DATA_DIR, filename)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def load_json(filename):
    """Load data from a JSON file inside the data folder.

    Returns an empty list if the file does not exist,
    is empty, or contains invalid JSON.
    """

    path = os.path.join(DATA_DIR, filename)

    # If the file doesn't exist yet, there's nothing to load
    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        content = f.read().strip()

    # Handle an empty file
    if not content:
        return []

    # Handle a file with broken/invalid JSON
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print(f"Warning: '{filename}' contains invalid JSON. Returning empty list.")
        return []
