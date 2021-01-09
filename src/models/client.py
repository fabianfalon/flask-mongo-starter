import jwt
import uuid
from flask import current_app
from mongoengine import Document, StringField, DateTimeField
from datetime import datetime
from src.constants import (
    ACTIVE,
    INACTIVE,
    CLIENT_NAME_MAX_LENGTH,
    CLIENT_DESCRIPTION_MAX_LENGTH,
    CLIENT_STATUS_MAX_LENGTH,
)
from src.exceptions import Unauthorized


class Client(Document):
    internal_id = StringField(default=uuid.uuid4())
    status_list = ((ACTIVE, "Active client"), (INACTIVE, "Inactive client"))
    name = StringField(required=True, max_length=CLIENT_NAME_MAX_LENGTH)
    description = StringField(required=True, max_length=CLIENT_DESCRIPTION_MAX_LENGTH)
    status = StringField(
        max_length=CLIENT_STATUS_MAX_LENGTH, choices=status_list, required=True
    )
    token = StringField()
    created = DateTimeField(default=datetime.now)

    def encode_token(self):
        try:
            payload = {
                "iat": datetime.utcnow(),
                "payload": {"external_id": self.internal_id, "status": self.status},
            }
            token = jwt.encode(
                payload, current_app.config.get("SECRET_KEY"), algorithm="HS256"
            )
            return token.decode("utf-8")
        except Exception as e:
            return e

    @staticmethod
    def decode_token(token: str):
        """
        Validates the auth token
        :param token:
        """
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))
            client_data = payload.get("payload")
            if client_data.get("status") == ACTIVE and client_data.get("external_id"):
                return payload
            else:
                raise Unauthorized(message="Client Inactive.")
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False
