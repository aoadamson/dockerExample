import json
from pprint import pprint

test_list = [
    '{"name": "Austin", "address": "1100 forth st", "ssn": "123-45-6789", "cardInfo": 1234123412341234}',
    '{"name": "Austin", "address": "1100 forth st", "ssn": "123-45-6789", "cardInfo": 1234123412341234}'
]


def parse_list_of_json_strings():
    result_list = [json.loads(i) for i in test_list]
    pprint(result_list)


parse_list_of_json_strings()

