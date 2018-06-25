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
# @todo: Forgot password

from flask import request, url_for, redirect, session, flash, abort, render_template

from flask_login import current_user, login_user, logout_user, login_required

from openapprentice import application
from openapprentice.models.user import User, UserLoginFlask, get_user
from openapprentice.forms.login import LoginForm
from openapprentice.utils.url import is_safe_url


@application.route('/login', methods=['POST', 'GET'])
def login():
    """
    The login view, called when a user is required to login. You can login usingyour email and password

    :return: Redirects to /home if the login is successfull. Otherwise, renders the login form and template
    """
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(User.email == form.email.data.encode("utf-8").lower())
        user.is_authenticated = True
        user.save()
        user = UserLoginFlask(user.uuid)
        login_user(user)
        flash("Successfully logged in !", "success")
        if not user.is_confirmed:
            return redirect(url_for("unconfirmed"))
        next_url = request.args.get('next')
        if not is_safe_url(next_url):
            return abort(400)
        if user.scope == "admin":
            return redirect(url_for("admin_dashboard"))
        return redirect(next_url or url_for('home'))
    return render_template('user/login.html', form=form)


@application.route("/logout")
@login_required
def logout():
    """
    This view will logout any user logged in.
    :return: Redirects to /login when the user is successfully logged out
    """

    user = get_user(current_user.uuid)
    user.is_authenticated = False
    user.save()
    logout_user()

    session.pop('id', None)
    session.pop('uid', None)
    session.pop('uuid', None)
    session.pop('userid', None)
    session.pop('user_id', None)
    session.pop('access_token', None)
    session.clear()
    flash("Successfully logged out ! See you soon !", "info")
    return redirect(url_for("home"))
