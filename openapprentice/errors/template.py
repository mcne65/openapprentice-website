# -*- coding: utf-8 -*-

"""
    The OpenApprentice Foundation and its website OpenApprentice.org
    Copyright (C) 2018 The OpenApprentice Foundation - contact@openapprentice.org

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
