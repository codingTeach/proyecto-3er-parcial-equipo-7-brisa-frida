from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://200300606:uaOPE866Q05En2b6@cluster.ukkl1.mongodb.net/?retryWrites=true&w=majority")
    db = client.sample_airbnb
    return db
