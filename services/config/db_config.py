from pymongo import MongoClient


client = MongoClient("mongodb+srv://200300606:uaOPE866Q05En2b6@cluster.ukkl1.mongodb.net/?retryWrites=true&w=majority")
db = client['sample_airbnb'] 
def get_db():
    return db
