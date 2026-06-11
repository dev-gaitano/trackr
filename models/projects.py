import json

class Project:
    all_projects = []
    FILE_PATH = 'data/projects.json'

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        Project.all_projects.append(self)

    def __repr__(self):
        return f'Project: {self.name}'

    def save_to_json(self):
        with open(self.FILE_PATH, 'r') as f:
            existing_data = json.load(f)
        existing_data[self.id] = {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
        with open(self.FILE_PATH, 'w') as f:
            json.dump(existing_data, f, indent=4)
            print(f'{self} saved successfully')

    @classmethod
    def read_from_json(cls):
        with open(cls.FILE_PATH, 'r') as f:
            data = json.load(f)
        print(data)
        all_projects = [cls(**project_info) for project_info in data.values()]
        return all_projects