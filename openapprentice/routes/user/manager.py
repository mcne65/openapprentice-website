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

from flask import session

from flask_login import LoginManager

from openapprentice import application
from openapprentice.models.user import UserLoginFlask
from openapprentice.errors import notfound

# Sets up the login manager.
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(uid):
    """
    Callback to reload the user
    :param uid: The uid to reload
    :return: Returns a user object corresponding to `uid` or None if the user doesn't exist.
    """

    # Dirty way to deal with a weird bug where it would remember the user_id when logging out
    if not session.get("_fresh"):
        return None
    try:
        user = UserLoginFlask(uid)
    except notfound.NotFoundError:
        return None
    else:
        return user
