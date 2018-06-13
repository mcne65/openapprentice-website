from template import generate_error_json

from openapprentice import application


class ConflictError(Exception):
    """
    This is the ConflictError class for the Exception.
    """
    def __init__(self, msg, solution):
        self.msg = msg
        self.solution = solution
        self.status_code = 409
    pass


@application.errorhandler(ConflictError)
def generate_conflict(error):
    """
    This is the 409 response creator. It will create a 409 response along with
    a custom message and the 409 code

    :param error: The error body
    :return: Returns the response formatted
    """

    return generate_error_json(error, 409)
