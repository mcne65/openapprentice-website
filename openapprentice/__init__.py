from flask import Flask

SECRET_KEY = 'ThisIsADevelopmentKey'
DEBUG = True

application = Flask(__name__)
application.debug = DEBUG
application.secret_key = SECRET_KEY

from routes import main
