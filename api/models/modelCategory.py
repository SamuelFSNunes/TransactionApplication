
class Category:
    def __init__(self,
                 name: str,
                 description:str = None) -> None:
        self.name = name
        self.description = description

    def __str__(self):
        return self.name