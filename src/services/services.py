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
