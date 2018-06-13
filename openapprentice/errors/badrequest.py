from openapprentice import application

from template import generate_error_json


class BadRequestError(Exception):
    """
    This is the BadRequestError class for the Exception.
    """
    def __init__(self, msg, solution):
        self.msg = msg
        self.solution = solution
        self.status_code = 400
    pass


@application.errorhandler(BadRequestError)
def generate_badrequest(error):
    """
    This is the 400 response creator. It will create a 400 response along with
    a custom message and the 400 code

    :param error: The error body
    :return: Returns the response formatted
    """
    return generate_error_json(error, 400)
