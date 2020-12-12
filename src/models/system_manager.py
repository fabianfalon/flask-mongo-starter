from mongoengine import Document, DictField, DateTimeField
from datetime import datetime


class SystemManager(Document):
    json = DictField(required=True)
    created = DateTimeField(default=datetime.now)
