import json

class User:
    all_users = []
    FILE_PATH = 'data/users.json'

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        User.all_users.append(self)
        pass

    def __repr__(self):
        return f'User: {self.name}'

    def save_to_json(self):
        with open(self.FILE_PATH, 'r') as f:
            existing_data = json.load(f)

        existing_data[self.id] = {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

        with open(self.FILE_PATH, 'w') as f:
            json.dump(existing_data, f, indent=4)
            print(f'{self} saved successfully')
        pass

    @classmethod
    def read_from_json(cls):
        with open(cls.FILE_PATH, 'r') as f:
            data = json.load(f)
        print(data)

        all_users = [cls(**user_info) for user_info in data.values()]
        return all_users
        pass