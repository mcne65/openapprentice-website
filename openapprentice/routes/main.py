from flask import render_template, redirect, url_for

from openapprentice import application
from ..forms import contact

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


@application.route('/ContactUs', methods=['GET', 'POST'])
def contact_us():
    """
    View called when a new scope needs to be created
    """

    form = contact.ContactForm()
    if form.validate_on_submit():
        print(form)
        return redirect(url_for('home'))
    return render_template("contact.html", form=form)
