from mongoengine import Document, DictField, DateTimeField, ListField, StringField
from datetime import datetime


class SystemManager(Document):
    external_id = StringField(required=False)
    vendor = StringField(required=False)
    sku = StringField(required=False)
    emei = StringField(required=False)
    simSerialNumber = StringField(required=False)
    enclosureSerialNumber = StringField(required=False)
    workingState = StringField(required=False)
    createdAt = StringField(required=False)
    setupStatus = StringField(required=False)
    pendingSystemStatus = StringField(required=False)
    systemId = StringField(required=False)
    installerId = StringField(required=False)
    installerName = StringField(required=False)
    companyId = StringField(required=False)
    companyName = StringField(required=False)
    devices = ListField(required=False)
    solarStrings = ListField(required=False)
    systemConfig = DictField(required=False)
    location = DictField(required=False)
    created = DateTimeField(default=datetime.now)
