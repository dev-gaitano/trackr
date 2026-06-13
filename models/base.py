import json
import os

DATA_DIR = "data"


class BaseModel:
    """Base class for all models providing persistence logic."""

    FILE_PATH = ""

    def __init__(self, id):
        self.id = id

    def save(self, data):
        """Saves individual record to the JSON file."""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        all_data = self.load_all()
        all_data[str(self.id)] = data

        try:
            with open(self.FILE_PATH, "w") as f:
                json.dump(all_data, f, indent=4)
        except IOError as e:
            print(f"Error saving data to {self.FILE_PATH}: {e}")

    @classmethod
    def load_all(cls):
        """Loads all records from the JSON file."""
        if not os.path.exists(cls.FILE_PATH):
            return {}
        try:
            with open(cls.FILE_PATH, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
        except IOError as e:
            print(f"Error reading data from {cls.FILE_PATH}: {e}")
            return {}

    @classmethod
    def find_by_id(cls, record_id):
        """Finds a record by its ID."""
        data = cls.load_all()
        record_data = data.get(str(record_id))
        if record_data:
            return cls(**record_data)
        return None

    @classmethod
    def get_all(cls):
        """Returns a list of all instances."""
        data = cls.load_all()
        return [cls(**item) for item in data.values()]
