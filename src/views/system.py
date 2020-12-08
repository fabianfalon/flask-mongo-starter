import logging
from src.serializers.system import SystemSchema
from flask_restplus import Namespace, Resource
from src.services.systems import system_srv
from src.helpers import response_list
API_SYSTEM = Namespace("systems", description="systems operations")

TAG_WRAPPER = "system"
TAG_LIST_WRAPPER = "systems"

logger = logging.getLogger("systems")


@API_SYSTEM.route("systems")
class Systems(Resource):

    def get(self):
        """Get all Systems"""
        systems = system_srv.all()
        logger.info("Get all systems")
        return response_list(
            TAG_LIST_WRAPPER,
            systems,
            serializer=SystemSchema,
        )
