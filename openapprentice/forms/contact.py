import re

from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError


# @todo: Split email validation
# @body: Move email regex in an utils file and the validator in a validator file.
def validate_email(form, field):
    email = field.data
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?))$", email) is not None:
            return
        else:
            raise ValidationError("Sorry, this email adress is not valid.")
    else:
        raise ValidationError("Sorry, this email adress is not valid.")


class ContactForm(FlaskForm):
    # @todo: Add a checkbox to send a copy of the message
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    email = StringField('Email Address', [validators.InputRequired(), validators.Email(), validate_email])
    message = StringField('Message', [validators.InputRequired()])

