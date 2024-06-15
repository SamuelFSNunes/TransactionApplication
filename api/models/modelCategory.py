
class Category:
    def __init__(self,
                 name: str,
                 description:str = None,
                 id=None) -> None:
        self.name = name
        self.description = description
        self.id = id

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            description=data["description"],
            id=str(data["_id"]) if "_id" in data else None
        )