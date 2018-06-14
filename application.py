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

This file is the main file used to run the application.
"""

import os
import logging

from openapprentice import application


def setup_logging():
    """
    Setup the logging with a good format.
    This also sets the warning level for the peewee module to WARNING as it would pollute the output
    """

    # This is the config used to format our logs.
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S')

    logging.getLogger("peewee").setLevel(logging.WARNING)
    # Send a message to flash that the server (re)starts.
    logging.info("************************************************************")
    logging.info("*********Starting new instance of OpenApprentice************")
    logging.info("************************************************************")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    debug = True
    setup_logging()
    application.run(host='0.0.0.0', port=port, debug=debug)
