from mongoengine import Document

class Repository:
    def __init__(self, model: Document):
        self.model = model

    def get_all(self):
        return list(self.model.objects.all())

    def get_by_id(self, object_id):
        return self.model.objects(id=object_id).first()

    def create(self, data):
        obj = self.model(**data)
        obj.save()
        return obj

    def update(self, object_id, data):
        obj = self.model.objects(id=object_id).first()
        if obj:
            obj.update(**data)
            obj.reload()
        return obj

    def delete(self, object_id):
        obj = self.model.objects(id=object_id).first()
        if obj:
            obj.delete()
        return obj