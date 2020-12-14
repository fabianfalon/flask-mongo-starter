from marshmallow import Schema, fields


class SystemSchema(Schema):

    id = fields.Str()
    vendor = fields.Str()
    sku = fields.Str()
    emei = fields.Str()
    simSerialNumber = fields.Str()
    enclosureSerialNumber = fields.Str()
    workingState = fields.Str()
    createdAt = fields.Str()
    setupStatus = fields.Str()
    setupState = fields.Str()
    installerId = fields.Str()
    installerName = fields.Str()
    companyId = fields.Str()
    companyName = fields.Str()
    devices = fields.List(fields.Dict())
    solarStrings = fields.List(fields.Dict())
    systemConfig = fields.Dict()
    location = fields.Dict()
