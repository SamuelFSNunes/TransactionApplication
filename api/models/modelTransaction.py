from datetime import datetime
from api.models.modelCategory import Category
from api.models.modelUser import User

class Transaction:
    def __init__(self, user: User, 
                 categoria: Category,
                amount: float, 
                date: datetime = None, 
                description: str = None) -> None:
        self.user = user
        self.categoria = categoria
        self.amount = amount
        self.date = date or datetime.now()
        self.description = description

    def __str__(self):
        return f"{self.user.name} - {self.amount}"