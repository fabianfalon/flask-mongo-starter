from mongoengine import Document, StringField, DateTimeField, BooleanField
from datetime import datetime


class Client(Document):
    status_list = (("ACTIVE", "Active client"), ("INVACTIVE", "Inactive client"))
    name = StringField(required=True, max_length=200)
    description = StringField(required=True)
    status = StringField(max_length=50, choices=status_list, required=True)
    created = DateTimeField(default=datetime.now)
