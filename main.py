# Create a random JSON file to test the mongoDB data access
import json
from pymongo import MongoClient


def save_file_to_database():

    client = MongoClient('localhost', 27017)
    db = client['crawler-test']
    collection = db['test']

    """
    client = MongoClient('mongodb://crawler:pwp21@127.0.0.1:27017/')
    db = client['crawler-pwp21']
    collection = db['test-file-import']
    """

    with open('json_testfile.json') as file:
        file_data = json.load(file)

    collection.insert_many(file_data)

    client.close()


save_file_to_database()


