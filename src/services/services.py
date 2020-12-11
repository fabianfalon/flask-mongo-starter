""""
Service
"""
import logging

logger = logging.getLogger("services")


class Service:
    def all(self):
        return NotImplemented

    def create(self, data):
        return NotImplemented

    def get_by_id(self, entity_id: int):
        return NotImplemented
