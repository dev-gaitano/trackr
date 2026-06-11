import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def save_json(filename, data):
    """Save data as JSON to data/<filename>."""
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def load_json(filename):
    """Load and return JSON data from data/<filename>."""
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)
