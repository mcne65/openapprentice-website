from template import generate_error_json

from openapprentice import application


class UnauthorizedError(Exception):
    """
    This is the UnauthorizedError class for the Exception.
    """
    def __init__(self, msg, solution):
        self.msg = msg
        self.solution = solution
        self.status_code = 401
    pass


@application.errorhandler(UnauthorizedError)
def generate_unauthorized(error):
    """
    This is the 401 response creator. It will create a 401 response with
    a custom message and the 401 code.

    :param error: The error body
    :return: Returns the response formatted
    """

    return generate_error_json(error, 401)

