#!/usr/bin/python
import sys

sys.path.insert(0, '/var/www/vhosts/website-staging')
activate_this = '/var/www/vhosts/website-staging/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from openapprentice import application
