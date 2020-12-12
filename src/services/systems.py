""""
System Service
"""
import logging

from src.services.services import Service
from src.models.system_manager import SystemManager

logger = logging.getLogger("services")


class SystemServices(Service):
    entity = SystemManager

    def create(self, data):
        system = SystemManager(json=data)
        system.save()
        logger.info("System created successfully")
        return system


system_srv = SystemServices()
