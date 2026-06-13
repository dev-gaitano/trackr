from models.base import BaseModel


class User(BaseModel):
    FILE_PATH = "data/users.json"

    def __init__(self, id, name, email):
        super().__init__(id)
        self.name = name
        self.__email = email  # Encapsulation

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value
        else:
            raise ValueError("Invalid email format")

    def save(self):
        data = {"id": self.id, "name": self.name, "email": self.email}
        super().save(data)

    def get_projects(self):
        """Relationship: User -> Projects"""
        from models.projects import Project

        all_projects = Project.get_all()
        return [p for p in all_projects if p.user_id == self.id]

    def __repr__(self):
        return f"<User: {self.name}>"
