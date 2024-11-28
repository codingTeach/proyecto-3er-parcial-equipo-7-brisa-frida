from pymongo import MongoClient
from bson.json_util import dumps
import json
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

class DataService:
    def __init__(self):
        # Conecta a MongoDB usando las variables de entorno
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('COLLECTION_NAME')]
        
        print("MONGO_URI:", os.getenv('MONGO_URI'))
        print("DB_NAME:", os.getenv('DB_NAME'))
        print("COLLECTION_NAME:", os.getenv('COLLECTION_NAME'))

    def get_all_data(self, page=1, per_page=10):
        """Obtiene todos los datos con paginación"""
        try:
            skip = (page - 1) * per_page
            data = self.collection.find({}).skip(skip).limit(per_page)
            return dumps(data)  # Devuelve los datos convertidos a JSON usando bson.json_util.dumps
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return dumps({"error": "Hubo un problema al obtener los datos"})

    def get_data_by_category(self, category, page=1, per_page=10):
        """Obtiene los datos por categoría con paginación"""
        try:
            skip = (page - 1) * per_page
            data = self.collection.find({"categoria": category}).skip(skip).limit(per_page)
            return dumps(data)  # Devuelve los datos convertidos a JSON
        except Exception as e:
            print(f"Error al obtener datos por categoría: {e}")
            return dumps({"error": "Hubo un problema al obtener los datos de la categoría"})

    def get_visualization_data(self, viz_type):
        """Obtiene datos para visualización"""
        try:
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
            
            # Realiza la consulta de agregación
            data = self.collection.aggregate(pipeline)
            return dumps(data)  # Devuelve los datos convertidos a JSON
        except Exception as e:
            print(f"Error en la visualización de datos: {e}")
            return dumps({"error": "Hubo un problema con la visualización de los datos"})
