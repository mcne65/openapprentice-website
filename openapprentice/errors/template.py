from flask import jsonify


def generate_error_json(error, status_code):
    """
    This function is used to generate a json of the error passed

    :param error: The error containing the message and solution
    :param status_code: The status code of the error.
    :return: Returns a json containing all the info
    """
    success = False
    json = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': error.msg,
            'solution': error.solution
        },
        'code': status_code

    }
    resp = jsonify(json)
    resp.status_code = status_code
    return resp
