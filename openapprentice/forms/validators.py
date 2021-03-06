# coding=utf-8
"""
This file contains all validators used by forms
"""

import re

from flask_babel import gettext

from openapprentice.models.user import get_user
from openapprentice.errors import notfound
from werkzeug.security import check_password_hash
from openapprentice.utils.password import password_check
from wtforms import ValidationError


def validate_email_exists(form, field):
    """
    This function will validate if the username entered is a valid one.

    :param form: The form
    :param field: the username field

    :return: Returns nothing if ok, else will raise a ValidationError
    """

    try:
        get_user(field.data)
    except notfound.NotFoundError:
        raise ValidationError(gettext('Unknown Email'))


def validate_password(form, field):
    """
    This function will validate if the password entered is correct and corresponds to the username entered.
    :param form: The form
    :param field: the password field
    :return: Returns nothing if ok, else will raise a ValidationError
    """
    try:
        user = get_user(form.email.data.encode("utf-8").lower())
    except notfound.NotFoundError:
        raise ValidationError(gettext("Invalid password"))
    if not check_password_hash(user.password, field.data.encode("utf-8")):
        raise ValidationError(gettext('Invalid password'))


def check_password_strengh(form, field):
    """
    This will check the password and return an error based on the results of password_check()
    :param form: The form
    :param field: The password field
    :return: Returns nothing if ok, else will raise a ValidationError
    """

    try:
        if form.disable_secure_password.data:
            return
    except AttributeError:
        pass

    results = password_check(field.data)
    if not results['password_ok']:
        if results['length_error']:
            raise ValidationError(gettext("Weak password: Length inferior to 8"))
        if results['digit_error']:
            raise ValidationError(gettext("Weak password: Missing at least 1 digit"))
        if results['uppercase_error']:
            raise ValidationError(gettext("Weak password: Missing at least 1 uppercase character"))
        if results['lowercase_error']:
            raise ValidationError(gettext("Weak password: Missing at least 1 lowercase character"))
        if results['symbol_error']:
            raise ValidationError(gettext("Weak password: Missing at least 1 special symbol (eg. !@#$%^&*.)"))


def validate_is_email_available(form, field):
    """
    This function will validate if the username is available
    :param form: The form
    :param field: The username field
    :return: Returns nothing if it's ok, otherwise will raise a ValidationError
    """

    if not field.data:
        raise ValidationError(gettext("Field required."))
    try:
        get_user(field.data)
    except notfound.NotFoundError:
        pass
    else:
        raise ValidationError(gettext("Email taken."))


def validate_valid_email(form, field):
    email = field.data
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", email) is not None:
            return
        else:
            raise ValidationError(gettext("Sorry, this email adress is not valid."))
    else:
        raise ValidationError(gettext("Sorry, this email adress is not valid."))
