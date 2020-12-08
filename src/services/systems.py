""""
Service
"""
import logging
from src.helpers import mongo
from src.services.services import Service
logger = logging.getLogger("services")


class SystemServices(Service):

    def all(self):
        return mongo.db.system_manager.find({})

    def create(self, data):
        return mongo.db.system_manager.insert(data)


system_srv = SystemServices()
