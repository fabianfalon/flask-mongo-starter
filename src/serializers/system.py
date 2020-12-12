from marshmallow import Schema, fields


class SystemSchema(Schema):
    id = fields.Str()
    json = fields.Dict()
    created = fields.Str()
