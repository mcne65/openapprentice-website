#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '/var/www/vhosts/website-staging')
activate_this = '/var/www/vhosts/website-staging/bin/activate_this.py'

exec(open(activate_this).read())

from openapprentice import application
