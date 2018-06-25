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

from datetime import datetime

from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from itsdangerous import URLSafeTimedSerializer
from itsdangerous import BadHeader, BadData, BadSignature, BadTimeSignature, SignatureExpired, BadPayload

from openapprentice import application
from openapprentice.utils import generate_email, send_email
from openapprentice.models.user import get_user


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


@application.route('/confirm/<token>')
def confirm_email(token):
    """
    This route takes a token in and checks if it works.
    If it is expired, redirects to the unconfirmed. otherwise log the user in

    :param token: The token from the email
    """

    try:
        email = confirm_token(token)
    except (BadHeader,
            BadData,
            BadSignature,
            BadTimeSignature,
            SignatureExpired,
            BadPayload):
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for("login"))
    user = get_user(email)
    if user.is_confirmed:
        flash('Account already confirmed. Please login.', 'success')
        return redirect(url_for("login"))
    else:
        user.is_confirmed = True
        user.confirmed_on = datetime.now()
        user.confirmed_by = "email"
        user.save()
        flash('You have confirmed your account. Thanks!', 'success')
        return redirect(url_for('login'))


@application.route('/unconfirmed')
@login_required
def unconfirmed():
    """
    This routes is used when a user isn't confirmed.
    """

    if current_user.is_confirmed:
        return redirect(url_for('home'))
    flash('Please confirm your account!', 'warning')
    return render_template('email/unconfirmed.html')


@application.route('/resend')
@login_required
def resend_confirmation():
    """
    This route will resend a confirmation email to the current_user
    """

    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html_email = generate_email(
        preview_text="Confirm your account - OpenApprentice",
        has_top_text=True,
        line1="Please confirm your account on OpenApprentice",
        line2="Follow this link to confirm your account. This link will expire in one hour.",
        has_button=True,
        button_url=confirm_url,
        button_message="Confirm",
        has_bottom_text=False,
    )
    send_email(current_user.email, "Confirm your account - OpenApprentice", html_email)

    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('unconfirmed'))

# @todo: Make it so email template can be translated too
