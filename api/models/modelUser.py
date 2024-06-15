class User:
    def __init__(self, email, name=None, password=None, id=None):
        self.name = name
        self.email = email
        self.password = password
        self.id = id

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            id=str(data["_id"]) if "_id" in data else None
        )
    
    def check_password(self, password):
        return self.password == password