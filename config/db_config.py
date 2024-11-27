from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://<mi_usuario>:<mi_contraseña>@cluster0.mongodb.net/analisis_datos?retryWrites=true&w=majority")
    db = client.analisis_datos
    return db
