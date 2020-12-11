""""
Service
"""
import logging

from bson.errors import InvalidId
from bson.objectid import ObjectId
from src.helpers import mongo
from src.services.services import Service
from src.exceptions import ResourceNotFound

logger = logging.getLogger("services")


class SystemServices(Service):
    def all(self, page_size: int, page_key: int):
        return mongo.db.system_manager.find().skip(page_key).limit(page_size)

    def create(self, data):
        system_id = mongo.db.system_manager.insert(data)
        system = mongo.db.system_manager.find_one({"_id": system_id})
        return system

    def get_by_id(self, entity_id: int):
        try:
            return mongo.db.system_manager.find_one({"_id": ObjectId(entity_id)})
        except InvalidId:
            raise ResourceNotFound(
                message="System with id: {id} not found".format(id=entity_id)
            )


system_srv = SystemServices()
