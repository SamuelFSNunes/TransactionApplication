from pymongo import MongoClient

class Repository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['mongodatabase']
        self.collection = self.db['mongodatabase']

    def get_all(self):
        return list(self.collection.find({}, {'_id': 0}))

    def get_by_id(self, data_id):
        return self.collection.find_one({'id': data_id}, {'_id': 0})

    def create(self, data):
        self.collection.insert_one(data)

    def update(self, data_id, new_data):
        self.collection.update_one({'id': data_id}, {'$set': new_data})

    def delete(self, data_id):
        self.collection.delete_one({'id': data_id})