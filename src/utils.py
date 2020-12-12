import requests
from flask import request
from functools import wraps
from src.exceptions import Unauthorized, BadRequest
from src.models.client import Client


def check_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_header = request.headers["Authorization"]
        if not token_header:
            raise BadRequest(message="Missing Authorization in headers.")

        # Remove the 'Basic" part from the token
        auth_token = token_header.split(maxsplit=1)[1]
        token = Client.decode_auth_token(auth_token)
        if not token:
            raise Unauthorized(message="Provide a valid auth token.")
        return f(*args, **kwargs)
    return decorated
