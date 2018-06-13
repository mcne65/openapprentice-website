from template import generate_error_json

from openapprentice import application


class ForbiddenError(Exception):
    """
    This is the ForbiddenError class for the Exception.
    """
    def __init__(self, msg, solution):
        self.msg = msg
        self.solution = solution
        self.status_code = 403
    pass


@application.errorhandler(ForbiddenError)
def generate_forbidden(error):
    """
    This is the 403 response creator. It will create a 403 response along with
    a custom message and the 403 code

    :param error: The error body
    :return: Returns the response formatted
    """

    return generate_error_json(error, 403)
