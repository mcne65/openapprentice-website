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

from openapprentice import application
from openapprentice.forms import contact
from openapprentice.utils.email import generate_email, send_email


@application.route('/index')
@application.route('/home')
@application.route('/main')
@application.route('/')
def home():
    """
    Renders the home template
    """
    return render_template("main/home.html")


@application.route("/apprentice_system")
def apprentice_system():
    """
    Renders the apprentice system template
    """
    return render_template("main/apprentice_system.html")


@application.route("/learning")
def learning():
    """
    Renders the learning template
    """
    return render_template("main/learning.html")


@application.route("/recruiters")
def recruiters():
    """
    Renders the recruiters template
    """
    return render_template("main/recruiters.html")


@application.route("/teachers")
def teachers():
    """
    Renders the teachers template
    """
    return render_template("main/teachers.html")


@application.route("/sponsors")
def sponsors():
    """
    Renders the sponsors template
    """
    return render_template("main/sponsors.html")


@application.route("/mission")
def mission():
    """
    Renders the mission template
    """
    return render_template("main/mission.html")


@application.route("/team")
def team():
    """
    Renders the team template
    """
    return render_template("main/team.html")


@application.route('/ContactUs', methods=['GET', 'POST'])
def contact_us():
    """
    Renders the contact form and sends an email
    """
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
        send_email("contact@openapprentice.org", "New message from {} {}".format(first_name, last_name), html_email)
        flash("Email sent ! We'll get back to you shortly !", "success")
        return redirect(url_for("home"))
    return render_template("main/contact.html", form=form)
