# coding=utf-8

"""
This file will contain all the forms needed to act on a user.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators
from openapprentice.forms.validators import validate_is_email_available, check_password_strengh


class NewUserForm(FlaskForm):
    """
    This class corresponds to the form rendered in `/register`.
    """

    email = StringField('Email Address', [validators.Email(), validators.InputRequired(), validate_is_email_available])
    password = PasswordField('New Password', [
        validators.InputRequired(),
        check_password_strengh,
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    disable_secure_password = BooleanField('Disable secure password check?')
    #recaptcha = RecaptchaField()
