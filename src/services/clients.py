""""
Client Service
"""
import logging
import uuid
from src.exceptions import BadRequest
from src.services.services import Service
from src.models.client import Client

logger = logging.getLogger("clients")


class ClientServices(Service):

    entity = Client

    def create(self, data: dict) -> Client:
        if not data.get("name"):
            raise BadRequest(message="name is required")
        client = self.entity(
            internal_id=str(uuid.uuid4()),
            name=data.get("name"),
            description=data.get("description"),
            status=data.get("status", "INACTIVE"),
        )
        client.save()
        client.token = client.encode_token()
        client.save()
        logger.info("Client created successfully")
        return client


client_srv = ClientServices()
