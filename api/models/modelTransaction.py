from datetime import date, datetime
from api.models.modelCategory import Category

class Transaction:
    def __init__(self,
                category: Category,
                amount: float, 
                date: datetime = None, 
                description: str = None,
                id = None) -> None:
        self.category = category
        self.amount = amount
        self.date = date or datetime.now().date()
        self.description = description
        self.id = id

    def __str__(self):
        return f"{self.category.name} - {self.amount}"
    
    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
            "description": self.description
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            category=data["category"],
            amount=data["amount"],
            date=data["date"],
            description=data["description"],
            id=str(data["_id"]) if "_id" in data else None
        )