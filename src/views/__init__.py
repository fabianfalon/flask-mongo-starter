from flask import Blueprint
from flask_restplus import Api
from src.constants import API_VERSION
from src.exceptions import APIException
from src.views.system import API_SYSTEM as system_ns

URL_PREFIX = f"/api/{API_VERSION}/"

HTTP_500_INTERNAL_SERVER_ERROR = 500

BLUEPRINT = Blueprint("api", __name__)

API = Api(
    BLUEPRINT,
    title="Systems Microservice",
    version=API_VERSION,
    description="Microservice to system manager",
    add_specs=True,
    authorizations={},
)


# Registers resources from namespace for current instance of api.
API.add_namespace(system_ns, path=URL_PREFIX)


@API.errorhandler(APIException)
def generic_api_error_handler(exception):
    """
    """
    json_message = {"messages": [exception.to_dict()]}
    return json_message, exception.status_code


@API.errorhandler
def generic_error_handler(exception):
    """
    """
    api_exception = APIException(code=type(exception).__name__, message=str(exception), error_type="CRITICAL")
    json_message = {"messages": [api_exception.to_dict()]}
    return json_message, HTTP_500_INTERNAL_SERVER_ERROR
