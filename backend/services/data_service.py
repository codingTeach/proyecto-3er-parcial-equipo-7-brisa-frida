from config.db_config import get_db

db = get_db()

def get_all_data():
    collection = db['datos']
    return list(collection.find({}, {'_id': 0}))

def get_data_by_category(category):
    collection = db['datos']
    return list(collection.find({"categoria": category}, {'_id': 0}))
