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


from flask_wtf import FlaskForm
from wtforms import StringField, validators
from flask_babel import gettext

from openapprentice.forms.validators import validate_valid_email


class ContactForm(FlaskForm):
    """
    This form is the one used to send an email to OpenApprentice
    """

    # @todo: Add a checkbox to send a copy of the message
    first_name = StringField(gettext('First Name'), [validators.InputRequired()])
    last_name = StringField(gettext('Last Name'), [validators.InputRequired()])
    email = StringField(gettext('Email Address'), [validators.InputRequired(), validators.Email(), validate_valid_email])
    message = StringField('Message', [validators.InputRequired()])

