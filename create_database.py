from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27018")
db = client['crawler-test-db']
collection = db['test']
