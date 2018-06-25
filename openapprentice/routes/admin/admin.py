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

from flask_login import current_user

from openapprentice import application
from openapprentice.models.user import get_user, User, create_user
from openapprentice.forms.user import NewUserForm
from openapprentice.decorators import admin_only, confirmed_required


@application.route("/admin")
@admin_only
@confirmed_required
def admin_dashboard():
    """
    Renders the home of the admin dashboard.
    This might in the future render some statistics etc
    """

    return render_template("admin/admin.html")


@application.route("/admin/users")
@admin_only
@confirmed_required
def user_list():
    """
    Displays the user list.
    Loops through the whole user DB and appends to a list every user id.
    Then renders the template with the variables passed
    """

    id_list = []
    for user in User.select():
        id_list.append(user.uuid)
    return render_template("admin/user_list.html", get_user=get_user, id_list=id_list)


@application.route("/admin/projects")
@admin_only
@confirmed_required
def projects():
    """
    Renders the project list for the admin dashboard.
    """
    return render_template("admin/projects.html")


@application.route("/admin/stats")
@admin_only
@confirmed_required
def stats():
    """
    Renders the stats for the admin dashboard
    """
    return render_template("admin/stats.html")


@application.route("/admin/new_user", methods=['GET', 'POST'])
@admin_only
@confirmed_required
def admin_new_user():
    """
    This view is called to create a new user.
    If the form is validated, a new user

    TODO: Checkbox to confirm user or send email to confirm it

    :return: Creates a new user and returns to the user list.
    """
    form = NewUserForm()
    if form.validate_on_submit():
        email = form.email.data.encode("utf-8").lower()
        password = form.password.data.encode("utf-8")

        user = create_user(email, password, "user")
        # This will disappear as users wont be confirmed by default but by email
        user.is_confirmed = True
        user.confirmed_on = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        user.confirmed_by = "admin"
        user.save()
        return redirect(url_for('user_list'))
    return render_template('admin/admin_new_user.html', form=form)


@application.route("/admin/users/delete/<uuid>")
@admin_only
@confirmed_required
def admin_delete_user(uuid):
    """
    This view is called with a user uuid to delete.
    If the user is different than admin OR himself, delete it.


    :param uuid: The uuid of the user to delete

    :return: Deletes the given user and returns to the user list
    """
    user = get_user(uuid)
    if user.email != "admin@openapprentice.org" or current_user.uuid != user.uuid:
        user.delete_instance()
    else:
        flash("This user cannot be deleted", category="error")
    return redirect(url_for("user_list"))


@application.route("/admin/users/promote/<uuid>")
@admin_only
@confirmed_required
def admin_promote_user(uuid):
    """
    This view is used to promote a user to the rank of admin.

    :param uuid: The uuid of the user to promote
    """
    user = get_user(uuid)
    if user.scope != "admin":
        user.scope = "admin"
        user.save()
    return redirect(url_for("user_list"))
