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

from flask import session, redirect, url_for, render_template, flash

from openapprentice import application
from openapprentice.forms.login import RegistrationForm
from openapprentice.models.user import create_user
from openapprentice.utils import generate_email, send_email
from openapprentice.routes.email.email import generate_confirmation_token


@application.route('/register', methods=['GET', 'POST'])
def register():
    """
    This view is called when a user wants/needs to register.
    :return: Renders the template to register or redirects to login if the login is successfull
    """
    if session.get('logged_in'):
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data.encode("utf-8").lower()
        password = form.password.data.encode("utf-8")

        user = create_user(email, password, "user")
        # This will disappear as users wont be confirmed by default but by email
        user.is_confirmed = False
        user.save()

        token = generate_confirmation_token(user.email)
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
        send_email(user.email, "Confirm your account - OpenApprentice", html_email)
        flash("Thanks for creating your account ! Please check your emails for a confirmation link !", "success")
        return redirect(url_for('login'))
    return render_template('user/register.html', form=form)
