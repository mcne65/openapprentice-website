from datetime import datetime

from flask import render_template, redirect, url_for

from openapprentice import application
from ..forms import contact
from ..utils import generate_email, send_email


@application.route('/index')
@application.route('/home')
@application.route('/main')
@application.route('/')
def home():
    return render_template("main.html")


@application.route("/learning")
def learning():
    return render_template("learning.html")


@application.route("/recruiters")
def recruiters():
    return render_template("recruiters.html")


@application.route("/about")
def about():
    return render_template("about.html")


@application.route("/team")
def team():
    return render_template("team.html")


@application.route('/ContactUs', methods=['GET', 'POST'])
def contact_us():
    form = contact.ContactForm()
    if form.validate_on_submit():
        time_sent = datetime.utcnow()
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
