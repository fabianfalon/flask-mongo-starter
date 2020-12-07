""""
Service
"""
import logging
from src.helpers import mongo

logger = logging.getLogger("services")


class Service:

    def all(self):
        return mongo.db.system_manager.find({})

    def create(self, data):
        return mongo.db.system_manager.insert(data)
