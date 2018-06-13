from template import generate_error_json

from openapprentice import application


class NotFoundError(Exception):
    """
    This is the NotFoundError class for the Exception.
    """
    def __init__(self, msg, solution):
        self.msg = msg
        self.solution = solution
        self.status_code = 404
    pass


@application.errorhandler(NotFoundError)
def generate_notfound(error):
    """
    This is the 404 response creator. It will create a 404 response with
    a custom message and the 404 code.

    :param error: The error body
    :return: Returns the response formatted
    """

    return generate_error_json(error, 404)

