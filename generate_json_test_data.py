import json
from faker import Faker
from random import randint
fake = Faker('de_DE')


def create_json_testfile():
    with open('json_testfile.json', 'w', encoding='utf-8') as output:
        test_data = []
        for _ in range(10):
            test_data.append({'id': randint(0, 100), 'name': fake.name()})
        json.dump(test_data, output, ensure_ascii=False, indent=2)


create_json_testfile()
