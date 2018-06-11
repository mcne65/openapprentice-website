from flask import render_template
from flask_mail import Message
from openapprentice import application, mail


def generate_email(preview_text=None,
                   has_top_text=False,
                   line1=None,
                   line2=None,
                   has_button=False,
                   button_url=None,
                   button_message=None,
                   has_bottom_text=False,
                   line3=None,
                   line4=None):
    """
    This function generates the html used to send emails.
    :param preview_text: Forced. The preview text rendered by some email viewers
    :param has_top_text: Boolean. Set to true if you want text before the button or the bottom text
    :param line1: Optional, only if has_top_text is true. The first text line.
    :param line2: Optional, only if has_top_text is true. The second text line.
    :param has_button: Boolean. Set to true if you want a button
    :param button_url: Optional, use only if has_button is True. The url of the button
    :param button_message: Optional, use only if has_button is True, The button text.
    :param has_bottom_text: Boolean. Set to true if you want text after the button or the top text
    :param line3: Optional, only if has_bottom_text is true. The third text line.
    :param line4: Optional, only if has_bottom_text is true. The fourth text line.
    :return: Returns the rendered html with the correct values

    @todo: Force one line when selecting top and/or bottom.
    @body This might make the if on the second and 4th line useless.

    """
    return render_template("email_template.html",
                           preview_text=preview_text,
                           has_top_text=has_top_text,
                           line1=line1,
                           line2=line2,
                           has_button=has_button,
                           button_url=button_url,
                           button_message=button_message,
                           has_bottom_text=has_bottom_text,
                           line3=line3,
                           line4=line4
                           )


def send_email(to, subject, template):
    """
    This function will send an email
    :param to: The recipient
    :param subject: The subject of the message
    :param template: The html template for the email
    """

    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=application.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)
