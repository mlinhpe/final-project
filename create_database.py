from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['crawler-test-db']
collection = db['test']
client.test.add_user('testuser', 'test123', roles=[{'role':'root','db':'test'}])
