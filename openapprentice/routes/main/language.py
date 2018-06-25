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

from flask import session, redirect, request, url_for, g, flash

from flask_login import current_user

from openapprentice import application, babel
from openapprentice import AVAILABLE_LANG


@application.route("/lang/<lang>")
def change_lang(lang):
    """
    The route called to change the language to display

    TODO: Secure lang change to only available languages

    :param lang: The language code to change to
    """

    session['lang'] = lang
    flash("Changed lang to {}".format(lang), "info")
    return redirect(request.referrer or url_for("home"))


@babel.localeselector
def get_locale():
    """
    Direct babel to use the language defined in the session.
    """
    return g.get('current_lang', 'en')


@application.before_request
def before():
    """
    Function executed before each request
    It sets the current language to either the lang set in the user profile or the one in the session
    """

    if current_user.is_anonymous and not current_user.is_authenticated:
        g.current_lang = session.get("lang")
    else:
        g.current_lang = session.get("lang") or current_user.locale
    g.available_lang = AVAILABLE_LANG
