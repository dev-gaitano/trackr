import json

class Task:
    all_tasks = []
    FILE_PATH = 'data/tasks.json'

    def __init__(self, id, title, description, status, project_id):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.project_id = project_id
        Task.all_tasks.append(self)

    def __repr__(self):
        return f'Task: {self.title} - {self.status}'

    def save_to_json(self):
        with open(self.FILE_PATH, 'r') as f:
            existing_data = json.load(f)
        existing_data[self.id] = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "project_id": self.project_id
        }
        with open(self.FILE_PATH, 'w') as f:
            json.dump(existing_data, f, indent=4)
            print(f'{self} saved successfully')

    @classmethod
    def read_from_json(cls):
        with open(cls.FILE_PATH, 'r') as f:
            data = json.load(f)
        print(data)
        all_tasks = [cls(**task_info) for task_info in data.values()]
        return all_tasks