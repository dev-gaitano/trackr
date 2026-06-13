from models.base import BaseModel


class Project(BaseModel):
    FILE_PATH = "data/projects.json"

    def __init__(self, id, name, description, user_id=None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.user_id = user_id

    def save(self):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id,
        }
        super().save(data)

    def get_tasks(self):
        """Relationship: Project -> Tasks"""
        from models.tasks import Task

        all_tasks = Task.get_all()
        return [t for t in all_tasks if t.project_id == self.id]

    def __repr__(self):
        return f"<Project: {self.name}>"
