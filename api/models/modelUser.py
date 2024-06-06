from mongoengine import Document, StringField, EmailField

class User(Document):
    name = StringField(max_length=100, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(max_length=100, required=True)

    def __str__(self):
        return self.name