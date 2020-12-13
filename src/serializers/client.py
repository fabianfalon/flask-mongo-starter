from marshmallow import Schema, fields


class ClientSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    description = fields.Str()
    status = fields.Str()
    token = fields.Str()
    created = fields.Str()
