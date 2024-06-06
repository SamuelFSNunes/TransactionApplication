from mongoengine import Document, StringField, DecimalField, ReferenceField, DateTimeField
from django.utils import timezone
from api.models.modelCategory import Category
from api.models.modelUser import User

class Transaction(Document):
    user = ReferenceField(User, required=True)
    categoria = ReferenceField(Category, required=True)
    amount = DecimalField(required=True, precision=2)
    date = DateTimeField(default=timezone.now)
    description = StringField()

    def __str__(self):
        return f"{self.user.name} - {self.amount}"