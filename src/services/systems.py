""""
Service
"""
import logging

from bson.errors import InvalidId
from bson.objectid import ObjectId
from src.services.services import Service
from src.exceptions import ResourceNotFound
from src.models.system_manager import SystemManager

logger = logging.getLogger("services")


class SystemServices(Service):
    entity = SystemManager

    def create(self, data):
        system = SystemManager(json=data)
        system.save()
        return system


system_srv = SystemServices()
