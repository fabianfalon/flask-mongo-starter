from mongoengine import Document, StringField, DateTimeField
from datetime import datetime
from src.constants import (
    CLIENT_NAME_MAX_LENGTH,
    CLIENT_DESCRIPTION_MAX_LENGTH,
    CLIENT_STATUS_MAX_LENGTH,
)


class Client(Document):
    status_list = (("ACTIVE", "Active client"), ("INVACTIVE", "Inactive client"))
    name = StringField(required=True, max_length=CLIENT_NAME_MAX_LENGTH)
    description = StringField(required=True, max_length=CLIENT_DESCRIPTION_MAX_LENGTH)
    status = StringField(
        max_length=CLIENT_STATUS_MAX_LENGTH, choices=status_list, required=True
    )
    created = DateTimeField(default=datetime.now)
