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
            entity = self.entity.objects.with_id(entity_id)
            if not entity:
                raise ResourceNotFound(
                    message="Entity with id: {id} not found".format(id=entity_id)
                )
            return entity
        except InvalidId:
            raise ResourceNotFound(
                message="Entity with id: {id} not found".format(id=entity_id)
            )
