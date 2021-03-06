class APIException(Exception):
    status_code = 400
    message = ""
    aliasError = "NotFound"

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["status_code"] = self.status_code
        rv["message"] = self.message
        rv["alias"] = self.aliasError
        return rv


class IntegrityError(APIException):
    pass


class ResourceNotFound(APIException):
    status_code = 404
    message = "Not found"
    aliasError = "NotFound"


class BadRequest(APIException):
    status_code = 400
    message = "Bad Request"
    aliasError = "BadRequest"


class Unauthorized(APIException):
    status_code = 401
    message = "Unauthorized"
    aliasError = "Unauthorized"
