from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, date

class Repository:
    def __init__(self, model, collection):
        self.model = model
        self.client = MongoClient('localhost:27017')
        self.db = self.client['mongodatabase']
        self.collection = self.db[collection]

    def get_all(self):
        documents = self.collection.find()
        return [self.model.from_dict(doc) for doc in documents]

    def get_by_id(self, object_id):
        document = self.collection.find_one({"_id": ObjectId(object_id)})
        if document:
            return self.model.from_dict(document)
        return None

    def create(self, data):
        obj = self.model(**data)
        obj_dict = obj.to_dict()
        result = self.collection.insert_one(obj_dict)
        obj_dict["id"] = result.inserted_id
        return self.model.from_dict(obj_dict)

    def update(self, object_id, data):
        obj_dict = self.convert_dates(data)

        result = self.collection.update_one(
            {"_id": ObjectId(object_id)},
            {"$set": obj_dict}
        )
        if result.matched_count:
            document = self.collection.find_one({"_id": ObjectId(object_id)})
            return self.model.from_dict(document)
        return None

    def delete(self, object_id):
        result = self.collection.delete_one({"_id": ObjectId(object_id)})
        return result.deleted_count > 0
    
    def convert_dates(self, data):
        converted_data = {}
        for key, value in data.items():
            if isinstance(value, date):  # Verifica se é uma instância de datetime.date
                converted_data[key] = datetime(value.year, value.month, value.day)
            else:
                converted_data[key] = value
        return converted_data

    def get_user_by_email_and_password(self, email, password):
        document = self.collection.find_one({"email": email, "password": password})
        return document