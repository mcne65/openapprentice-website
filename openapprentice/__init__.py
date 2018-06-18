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

This file contains all initialization needed to run the website.
"""

import os

from decouple import config

import peewee

from flask import Flask
from flask_mail import Mail
from flask_babel import Babel


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if "OA_CONTACT_EMAIL_PASSWORD" not in os.environ:
    raise EnvironmentError("OA_CONTACT_EMAIL_PASSWORD should be set with the password"
                           " for the email used to send emails.")

if "OA_DB_USER" not in os.environ:
    raise EnvironmentError("OA_DB_USER should be set with the user used to access the DB")

if "OA_DB_PASSWD" not in os.environ:
    raise EnvironmentError("OA_DB_PASSWD should be set with the password used to access the DB")


if not os.path.exists(ROOT_DIR + "/settings.ini"):
    raise EnvironmentError("file settings.ini not found ! {}".format(ROOT_DIR + "/../settings.ini"))

AVAILABLE_LANG = config('available', default="en", cast=str).split(",")

SECRET_KEY = 'ThisIsADevelopmentKey'
DEBUG = True

application = Flask(__name__)
application.debug = DEBUG
application.secret_key = SECRET_KEY

application.config['MAIL_SERVER'] = 'openapprentice.org'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USE_SSL'] = False
application.config['MAIL_USERNAME'] = 'contact@openapprentice.org'
application.config['MAIL_PASSWORD'] = os.environ.get("OA_CONTACT_EMAIL_PASSWORD")
application.config['MAIL_DEFAULT_SENDER'] = 'contact@openapprentice.org'

mail = Mail(application)
user_db = peewee.MySQLDatabase(
    "oa_users",
    password=os.environ.get("OA_DB_PASSWD", None),
    user=os.environ.get("OA_DB_USER", None)
)

babel = Babel(application)

from openapprentice.routes import main
