# Create a random JSON file to test the mongoDB data access
import json
from faker import Faker
from random import randint
from pymongo import MongoClient

fake = Faker('de_DE')


def create_json_testfile():
    with open('json_testfile.json', 'w', encoding='utf-8') as output:
        test_data = []
        for _ in range(10):
            test_data.append({'id': randint(0, 100), 'name': fake.name()})
        json.dump(test_data, output, ensure_ascii=False, indent=2)


create_json_testfile()


def save_file_to_database(filename: str):
    '''
    client = MongoClient('localhost', 27017)
    db = client['crawler-test']
    collection = db['test']
    '''

    client = MongoClient('mongodb://crawler:pwp21@127.0.0.1:27017/')
    db = client['crawler-pwp21']
    collection = db['test-file-import']

    with open(f'{filename}') as file:
        file_data = json.load(file)

    collection.insert_many(file_data)

    client.close()


save_file_to_database('json_testfile.json')


