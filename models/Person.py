from marshmallow import Schema, fields


class Person(Schema):
    name = fields.Str()
    address = fields.Str()
    ssn = fields.Str()
    cardInfo = fields.Int()
