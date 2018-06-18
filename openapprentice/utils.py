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

This file contains all utility function, classes and variables used throughout the program
"""

import string
import random
import re
import sys

from flask import render_template, request
from flask_mail import Message
from openapprentice import application, mail

if sys.version_info > (3, 0):
    from urllib.parse import urlparse, urljoin
else:
    from urlparse import urlparse, urljoin


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
    return render_template("email_template.html",
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


def is_safe_url(target):
    """
    Tests if the url to redirect to is safe
    :param target: the url to redirect to
    :return: True if the url is safe, False otherwise
    """

    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


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


def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    return {
        'password_ok': password_ok,
        'length_error': length_error,
        'digit_error': digit_error,
        'uppercase_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'symbol_error': symbol_error,
    }


def get_random_string(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
