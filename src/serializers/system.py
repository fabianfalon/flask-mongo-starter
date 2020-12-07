from marshmallow import Schema, fields


class SystemSchema(Schema):
    _id = fields.Str()
    name = fields.Str()
    status = fields.Str()
    description = fields.Str()
