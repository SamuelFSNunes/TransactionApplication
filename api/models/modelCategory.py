from mongoengine import Document, StringField

class Category(Document):
    name = StringField(max_length=100, required=True)
    description = StringField(required=False)

    def __str__(self):
        return self.name