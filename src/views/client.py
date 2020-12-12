import logging
from flask import request
from flask_restplus import Namespace, Resource, reqparse
from werkzeug.exceptions import BadRequest

from src.constants import MAX_ELEMENT_PAGINATION
from src.helpers import response_list, response_item
from src.serializers.client import ClientSchema
from src.services.clients import client_srv

API_CLIENT = Namespace("clients", description="clients operations")

TAG_WRAPPER = "client"
TAG_LIST_WRAPPER = "clients"

logger = logging.getLogger("clients")


@API_CLIENT.route("clients")
class Clients(Resource):
    @API_CLIENT.doc(
        description="Get all clients",
        response={
            200: "Recover all clients",
        },
        params={
            "paginationKey": {"description": "pagination_key", "type": "integer"},
            "pageSize": {"description": "pagination_size", "type": "integer"},
        },
    )
    def get(self):
        """Get all Clients"""
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
        clients = client_srv.all(page_size, pagination_key)
        logger.info("Get all clients")
        return response_list(TAG_LIST_WRAPPER, clients, serializer=ClientSchema)

    # @API_CLIENT.expect(MODEL_CREATE_USER, description="Input data")
    @API_CLIENT.doc(
        description="Create system",
        responses={
            201: "System created",
            400: "Input data wrong",
            500: "Internal Server Error",
        },
    )
    def post(self):
        logger.info("Create system")
        client_payload = request.get_json()
        client = client_srv.create(client_payload)
        data = response_item(TAG_WRAPPER, client, serializer=ClientSchema)
        return data, 201


@API_CLIENT.route("clients/<clientId>")
class SystemDetail(Resource):
    @API_CLIENT.doc(
        description="Get a client detail",
        responses={
            200: "Client detail",
            404: "Client Entity not found",
        },
    )
    def get(self, **kwargs):
        client_id = kwargs.get("clientId")
        system = client_srv.get_by_id(client_id)
        logger.info("Get client detail")
        return response_item(TAG_LIST_WRAPPER, system, serializer=ClientSchema)
