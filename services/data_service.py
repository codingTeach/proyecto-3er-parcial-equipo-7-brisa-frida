from pymongo import MongoClient
from bson.json_util import dumps
import json
import os
from dotenv import load_dotenv


load_dotenv()

class DataService:
    def __init__(self):
        
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('COLLECTION_NAME')]
        print("MONGO_URI:", os.getenv('MONGO_URI'))
        print("DB_NAME:", os.getenv('DB_NAME'))
        print("COLLECTION_NAME:", os.getenv('COLLECTION_NAME'))

    def get_all_data(self):
        data = self.collection.find({})
        return json.loads(dumps(data))

    def get_data_by_category(self, category):
        data = self.collection.find({"categoria": category})
        return json.loads(dumps(data))

    def get_visualization_data(self, viz_type):

        if viz_type == "categorias":
            pipeline = [
                {"$group": {"_id": "$categoria", "total": {"$sum": "$valor"}, "count": {"$sum": 1}}},
                {"$sort": {"total": -1}}
            ]
        elif viz_type == "temporal":
            pipeline = [
                {"$group": {"_id": {"year": {"$year": "$fecha"}, "month": {"$month": "$fecha"}}, "total": {"$sum": "$valor"}}},
                {"$sort": {"_id.year": 1, "_id.month": 1}}
            ]
        elif viz_type == "regional":
            pipeline = [
                {"$group": {"_id": "$region", "total": {"$sum": "$valor"}}},
                {"$sort": {"total": -1}}
            ]
        else:
            raise ValueError("Tipo de visualización no válido")
        
        data = self.collection.aggregate(pipeline)
        return json.loads(dumps(data))

   
    def insert_data(self, data):
        if isinstance(data, list):
            self.collection.insert_many(data)
        else:
            self.collection.insert_one(data)
        print("Datos insertados correctamente.")
