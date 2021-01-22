from pymongo import MongoClient
client = MongoClient()
db = client.primer
collection = db.dataset
