from faker import Faker
from pprint import pprint

faker = Faker()

mock_person = {
  "name": faker.name(),
  "address": faker.address(),
  "ssn": faker.ssn(),
  "cardInfo": faker.credit_card_number(),
  "bankAccountNumber": faker.bban(),
  "company": faker.company()
}

pprint(mock_person)
