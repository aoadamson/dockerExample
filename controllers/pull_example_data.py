import json
from models.Person import Person


def pull_data_example():
    with open("../data/data.json") as f:
        read_data = json.load(f)
        validated = Person().load(read_data)
        return validated


print(pull_data_example())
