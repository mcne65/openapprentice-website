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
"""

from datetime import datetime

from flask import render_template, redirect, url_for, session, request, abort, g
from flask_login import LoginManager, logout_user, login_required, login_user, current_user

from openapprentice import application, babel, AVAILABLE_LANG
from openapprentice.forms import contact
from openapprentice.forms.login import LoginForm, RegistrationForm
from openapprentice.forms.user import NewUserForm
from openapprentice.utils import generate_email, send_email, is_safe_url
from openapprentice.models.user import User, UserLoginFlask, get_user, create_user
from openapprentice.errors import notfound

# Sets up the login manager.
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"


@application.route('/index')
@application.route('/home')
@application.route('/main')
@application.route('/')
def home():
    return render_template("home.html")


@application.route("/apprentice_system")
def apprentice_system():
    return render_template("apprentice_system.html")


@application.route("/learning")
def learning():
    return render_template("learning.html")


@application.route("/recruiters")
def recruiters():
    return render_template("recruiters.html")


@application.route("/teachers")
def teachers():
    return render_template("teachers.html")


@application.route("/sponsors")
def sponsors():
    return render_template("sponsors.html")


@application.route("/mission")
def mission():
    return render_template("mission.html")


@application.route("/team")
def team():
    return render_template("team.html")


@application.route('/ContactUs', methods=['GET', 'POST'])
def contact_us():
    form = contact.ContactForm()
    if form.validate_on_submit():
        time_sent = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        email = form.email.data.encode('utf-8')
        message = form.message.data.encode('utf-8')
        first_name = form.first_name.data.encode('utf-8')
        last_name = form.last_name.data.encode('utf-8')
        line1 = "New message from {}:".format(email)

        # @todo: Add carriage returns to info on contact us email
        # @body: The current format is in one line. This needs to change
        info = "Sent by {} {}Sent at {}Reply to {}".format(first_name, last_name, time_sent, email)
        html_email = generate_email(
            preview_text="OpenApprentice got a new message",
            has_top_text=True,
            line1=line1,
            line2=message,
            has_button=True,
            button_url="mailto:{}".format(email),
            button_message="To reply, click me",
            has_bottom_text=True,
            line3="More info:",
            line4=info
        )
        send_email("OpenApprenticeFoundation@gmail.com", "New message.", html_email)
        return redirect(url_for("home"))

    return render_template("contact.html", form=form)


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
        #if not user.is_confirmed:
        #    flash("Sorry, you need to confirm your email adress {}.".format(user.email))
        #    logging.warn("User {} tried to login but email {} is not confirmed".format(user.name, user.email))
        #    return redirect(url_for("unconfirmed"))
        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)
        if user.scope == "admin":
            return redirect(url_for("admin_dashboard"))
        return redirect(next or url_for('home'))
    return render_template('login.html', form=form)


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

    return redirect(url_for("home"))


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
        user.is_confirmed = True
        user.confirmed_on = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        user.confirmed_by = "admin"
        user.save()
        #token = generate_confirmation_token(user.email)
        #confirm_url = url_for('confirm_email', token=token, _external=True)
        #html = render_template('activate_email.html', confirm_url=confirm_url)
        #subject = "Please confirm your email - unsupervised.ai"
        #send_email(user.email, subject, html)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# @todo: Forgot password


@application.route("/admin")
def admin_dashboard():
    return render_template("admin.html")


@application.route("/admin/users")
def user_list():
    id_list = []
    for user in User.select():
        id_list.append(user.uuid)
    return render_template("user_list.html", get_user=get_user, id_list=id_list)


@application.route("/admin/projects")
def projects():
    return render_template("projects.html")


@application.route("/admin/stats")
def stats():
    return render_template("stats.html")


@application.route("/lang/<lang>")
def change_lang(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for("home"))


@babel.localeselector
def get_locale():
    """Direct babel to use the language defined in the session."""
    return g.get('current_lang', 'en')


@application.before_request
def before():
    if current_user.is_anonymous and not current_user.is_authenticated:
        g.current_lang = session.get("lang")
    else:
        g.current_lang = session.get("lang") or current_user.locale
    g.available_lang = AVAILABLE_LANG


@application.route("/admin/new_user", methods=['GET', 'POST'])
def new_user():
    form = NewUserForm()
    if form.validate_on_submit():
        email = form.email.data.encode("utf-8").lower()
        password = form.password.data.encode("utf-8")

        user = create_user(email, password, "user")
        # This will disappear as users wont be confirmed by default but by email
        #user.is_confirmed = True
        #user.confirmed_on = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        #user.confirmed_by = "admin"
        user.save()
        #token = generate_confirmation_token(user.email)
        #confirm_url = url_for('confirm_email', token=token, _external=True)
        #html = render_template('activate_email.html', confirm_url=confirm_url)
        #subject = "Please confirm your email - unsupervised.ai"
        #send_email(user.email, subject, html)
        return redirect(url_for('user_list'))
    return render_template('admin_new_user.html', form=form)

# @todo: Make it so email template can be translated too


@application.route("/users/delete/<uuid>")
def admin_delete_user(uuid):
    user = get_user(uuid)
    user.delete_instance()
    return redirect(url_for("user_list"))

