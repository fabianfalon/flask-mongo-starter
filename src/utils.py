from functools import wraps

from flask import request

from src.exceptions import BadRequest, Unauthorized
from src.models.client import Client


def check_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_header = request.headers.get("Authorization", None)
        if not token_header:
            raise BadRequest(message="Missing Authorization in headers.")

        # Remove the 'Basic" part from the token
        auth_token = token_header.split(maxsplit=1)[1]
        token = Client.decode_token(auth_token)
        if not token:
            raise Unauthorized(message="Provide a valid auth token.")
        return f(*args, **kwargs)

    return decorated


authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}
