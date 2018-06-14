# -*- coding: utf-8 -*-

"""
    The OpenApprentice Foundation and its website OpenApprentice.org
    Copyright (C) 2018 David Kartuzinski - contact@openapprentice.org

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

