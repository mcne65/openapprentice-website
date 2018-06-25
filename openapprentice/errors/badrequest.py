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

from openapprentice import application
from openapprentice.errors.template import generate_error_json


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