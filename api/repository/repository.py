from pymongo import MongoClient
from bson.objectid import ObjectId

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
        obj_dict = {k: v for k, v in data.items() if v is not None}
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