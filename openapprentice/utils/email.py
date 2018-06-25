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

This file contains all utility function, classes and variables used throughout the program
"""

import re

from flask import render_template

from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from itsdangerous import BadHeader, BadData, BadSignature, BadTimeSignature, SignatureExpired, BadPayload

from openapprentice import application
from openapprentice import mail


def generate_confirmation_token(email):
    """
    This view will generate a confirmation token

    :param email: The email to serialize in the token

    :return: Returns a serialized token
    """

    serializer = URLSafeTimedSerializer(application.config['SECRET_KEY'])
    email_token = serializer.dumps(
        email, salt=application.config['SECURITY_PASSWORD_SALT'])
    return email_token


def confirm_token(token, expiration=3600):
    """
    This function will check if the token has expired or not.

    :param token: The token to check
    :param expiration: How old is the token allowed to be

    :return: Returns False if the token isn't accepted, returns the email
     otherwise
    """

    serializer = URLSafeTimedSerializer(application.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            # TODO: Secure password salt in env
            salt=application.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except (BadHeader, BadData, BadSignature, BadTimeSignature, SignatureExpired, BadPayload):
        return False
    return email


def generate_email(preview_text=None,
                   has_top_text=False,
                   line1=None,
                   line2=None,
                   has_button=False,
                   button_url=None,
                   button_message=None,
                   has_bottom_text=False,
                   line3=None,
                   line4=None):
    """
    This function generates the html used to send emails.
    :param preview_text: Forced. The preview text rendered by some email viewers
    :param has_top_text: Boolean. Set to true if you want text before the button or the bottom text
    :param line1: Optional, only if has_top_text is true. The first text line.
    :param line2: Optional, only if has_top_text is true. The second text line.
    :param has_button: Boolean. Set to true if you want a button
    :param button_url: Optional, use only if has_button is True. The url of the button
    :param button_message: Optional, use only if has_button is True, The button text.
    :param has_bottom_text: Boolean. Set to true if you want text after the button or the top text
    :param line3: Optional, only if has_bottom_text is true. The third text line.
    :param line4: Optional, only if has_bottom_text is true. The fourth text line.
    :return: Returns the rendered html with the correct values

    @todo: Force one line when selecting top and/or bottom.
    @body This might make the if on the second and 4th line useless.

    """
    return render_template("email/generic.html",
                           preview_text=preview_text,
                           has_top_text=has_top_text,
                           line1=line1,
                           line2=line2,
                           has_button=has_button,
                           button_url=button_url,
                           button_message=button_message,
                           has_bottom_text=has_bottom_text,
                           line3=line3,
                           line4=line4
                           )


def send_email(to, subject, template):
    """
    This function will send an email
    :param to: The recipient
    :param subject: The subject of the message
    :param template: The html template for the email
    """

    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=application.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)


def is_valid_email(email):
    """
    Tests with a regex if the email passed is valid
    :param email: The email to test
    :return: Returns False if the email isn't valid, True otherwise
    """
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", email) is not None:
            return True
    return False
