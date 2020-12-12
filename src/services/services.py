""""
Service
"""
import logging
from bson.errors import InvalidId
from src.exceptions import ResourceNotFound

logger = logging.getLogger("services")


class Service:

    entity = None

    def all(self, page_size: int, page_key: int):
        return self.entity.objects.all().skip(page_key).limit(page_size)

    def create(self, data):
        return NotImplemented

    def get_by_id(self, entity_id: int):
        try:
            return self.entity.objects.with_id(entity_id)
        except InvalidId:
            raise ResourceNotFound(
                message="Client with id: {id} not found".format(id=entity_id)
            )
