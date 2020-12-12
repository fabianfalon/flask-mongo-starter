""""
Client Service
"""
import logging

from src.exceptions import BadRequest
from src.services.services import Service
from src.models.client import Client

logger = logging.getLogger("clients")


class ClientServices(Service):

    entity = Client

    def create(self, data):
        if not data.get("name"):
            raise BadRequest(message="name is required")
        client = Client(
            name=data.get("name"),
            description=data.get("description"),
            status=data.get("status", "INACTIVE"),
        )
        client.save()
        logger.info("Client created successfully")
        return client


client_srv = ClientServices()
