import os

import peewee
from flask import Flask
from flask_mail import Mail


if "OA_GMAIL_PASSWORD" not in os.environ:
    raise EnvironmentError("OA_GMAIL_PASSWORD should be set with the password for the email used to send emails.")

if "OA_DB_USER" not in os.environ:
    raise EnvironmentError("OA_DB_USER should be set with the user used to access the DB")

if "OA_DB_PASSWD" not in os.environ:
    raise EnvironmentError("OA_DB_PASSWD should be set with the password used to access the DB")


SECRET_KEY = 'ThisIsADevelopmentKey'
DEBUG = True

application = Flask(__name__)
application.debug = DEBUG
application.secret_key = SECRET_KEY

application.config['MAIL_SERVER'] = 'smtp.googlemail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
application.config['MAIL_USERNAME'] = 'OpenApprenticeFoundation@gmail.com'
application.config['MAIL_PASSWORD'] = os.environ.get("OA_GMAIL_PASSWORD")
application.config['MAIL_DEFAULT_SENDER'] = 'OpenApprenticeFoundation@gmail.com'

mail = Mail(application)
user_db = peewee.MySQLDatabase(
    "oa_users",
    password=os.environ.get("OA_DB_PASSWD", None),
    user=os.environ.get("OA_DB_USER", "root")
)

from routes import main
