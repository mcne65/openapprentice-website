from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from openapprentice.forms.validators import validate_email, validate_is_email_available
from openapprentice.forms.validators import validate_password, check_password_strengh


class LoginForm(FlaskForm):
    """
    This class corresponds to the login form rendered in `/login`.
    """

    email = StringField('Email', [validators.InputRequired(), validate_email])
    password = PasswordField('Password', [validators.InputRequired(), validate_password])
    #recaptcha = RecaptchaField()


class RegistrationForm(FlaskForm):
    """
    This class corresponds to the form rendered in `/register`.
    """

    email = StringField('Email Address', [validators.Email(), validators.InputRequired(), validate_is_email_available])
    password = PasswordField('New Password', [
        validators.InputRequired(),
        check_password_strengh,
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    #recaptcha = RecaptchaField()
