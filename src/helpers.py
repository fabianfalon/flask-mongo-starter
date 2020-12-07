from flask_pymongo import PyMongo
from src.serializers.common import PaginationSchema

mongo = PyMongo()


def response_list(list_name, list_response, **kwargs):

    serializer = kwargs.get("serializer")
    schema = serializer()
    response = {"data": {list_name: schema.dump(list(list_response), many=True)}}
    return response


def response_list_paginated(
    list_name, pagination, serializer, base_link_pagination, **kwargs
):
    query_params = kwargs.get("query_params")

    items = pagination.items
    response = response_list(list_name, items, serializer=serializer)
    context = {
        "base_link_pagination": base_link_pagination,
        "query_params": query_params,
    }
    schema = PaginationSchema(context=context)
    pagination_field = schema.dump(pagination).data

    response["pagination"] = pagination_field
    return response
