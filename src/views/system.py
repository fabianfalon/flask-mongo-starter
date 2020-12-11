import logging
from flask import request
from flask_restplus import Namespace, Resource, reqparse
from werkzeug.exceptions import BadRequest

from src.constants import MAX_ELEMENT_PAGINATION
from src.helpers import response_list, custom_response
from src.serializers.system import SystemSchema
from src.services.systems import system_srv

API_SYSTEM = Namespace("systems", description="systems operations")

TAG_WRAPPER = "system"
TAG_LIST_WRAPPER = "systems"

logger = logging.getLogger("systems")


@API_SYSTEM.route("systems")
class Systems(Resource):
    @API_SYSTEM.doc(
        description="Get all systems",
        response={
            200: "Recover all systems",
        },
        params={
            "paginationKey": {"description": "pagination_key", "type": "integer"},
            "pageSize": {"description": "pagination_size", "type": "integer"},
        },
    )
    def get(self):
        """Get all Systems"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "pageSize",
            required=False,
            default=MAX_ELEMENT_PAGINATION,
            type=int,
            location="args",
        )
        parser.add_argument(
            "paginationKey", required=False, default=0, type=int, location="args"
        )
        params = {}
        try:
            args = parser.parse_args()
        except BadRequest as err:
            raise Exception(message=err.data["message"], parameters=err.data["errors"])

        params.update(
            {"pageSize": min(int(args.get("pageSize", 0)), MAX_ELEMENT_PAGINATION)}
        )
        params.update({"paginationKey": int(args.get("paginationKey", 1))})
        page_size = params.get("pageSize")
        pagination_key = params.get("paginationKey")
        systems = system_srv.all(page_size, pagination_key)
        logger.info("Get all systems")
        return custom_response(
            TAG_LIST_WRAPPER,
            systems,
        )

    # @API_SYSTEM.expect(MODEL_CREATE_USER, description="Input data")
    @API_SYSTEM.doc(
        description="Create system",
        responses={
            201: "System created",
            400: "Input data wrong",
            500: "Internal Server Error",
        },
    )
    def post(self):
        logger.info("Create system")
        system_payload = request.get_json()
        system = system_srv.create(system_payload)
        data = custom_response(TAG_WRAPPER, system, serializer=SystemSchema)
        return data, 201


@API_SYSTEM.route("systems/<systemId>")
class SystemDetail(Resource):
    @API_SYSTEM.doc(
        description="Get a system detail",
        responses={
            200: "System detail",
            404: "System Entity not found",
        },
    )
    def get(self, **kwargs):
        system_id = kwargs.get("systemId")
        system = system_srv.get_by_id(system_id)
        logger.info("Get system detail")
        return custom_response(TAG_LIST_WRAPPER, system)
