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

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators
from flask_babel import gettext

from openapprentice.forms.validators import validate_is_email_available, check_password_strengh


class NewUserForm(FlaskForm):
    """
    This class corresponds to the form rendered in `/register`.
    """

    email = StringField(gettext('Email Address'), [validators.Email(),
                                                   validators.InputRequired(),
                                                   validate_is_email_available])
    password = PasswordField(gettext('New Password'), [
        validators.InputRequired(),
        check_password_strengh,
        validators.EqualTo(gettext('confirm'), message=gettext('Passwords must match'))
    ])
    confirm = PasswordField(gettext('Repeat Password'))
    disable_secure_password = BooleanField(gettext('Disable secure password check?'))
    # recaptcha = RecaptchaField()


class Register(FlaskForm):
    """
    This class corresponds to the form rendered in `/register`.
    """

    email = StringField(gettext('Email Address'), [validators.Email(),
                                                   validators.InputRequired(),
                                                   validate_is_email_available])
    password = PasswordField(gettext('New Password'), [
        validators.InputRequired(),
        check_password_strengh,
        validators.EqualTo(gettext('confirm'), message=gettext('Passwords must match'))
    ])
    confirm = PasswordField(gettext('Repeat Password'))
    # recaptcha = RecaptchaField()
