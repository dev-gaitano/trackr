from models.base import BaseModel

class Task(BaseModel):
    FILE_PATH = 'data/tasks.json'

    def __init__(self, id, title, description, status, project_id=None):
        super().__init__(id)
        self.title = title
        self.description = description
        self.status = status
        self.project_id = project_id

    def save(self):
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "project_id": self.project_id
        }
        super().save(data)

    def __repr__(self):
        return f"<Task: {self.title} [{self.status}]>"
