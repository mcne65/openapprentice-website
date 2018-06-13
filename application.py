import os
import logging
from logging import DEBUG

from openapprentice import application

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_logging():
    # This is the config used to format our logs.
    logging.basicConfig(level=DEBUG,
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
