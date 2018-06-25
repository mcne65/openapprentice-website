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

from nose.tools import assert_raises, assert_equal
from wtforms import ValidationError

from openapprentice.forms.validators import check_password_strengh, validate_email_exists, validate_is_email_available
from openapprentice.forms.validators import validate_valid_email
from openapprentice.models.user import create_user
from openapprentice.utils.strings import get_random_string


random_email = get_random_string() + "@" + get_random_string() + ".com"


class FakeField:
    """
    Fake form field with random data
    """
    def __init__(self, data):
        self.data = data


def test_check_password_strengh_length():
    field = FakeField("shrtpwd")
    with assert_raises(ValidationError) as e:
        check_password_strengh(None, field)

    assert_equal(e.exception.args[0], "Weak password: Length inferior to 8")


def test_check_password_strengh_at_least_one_digit():
    field = FakeField("longenoughpasswordbutnodigit")
    with assert_raises(ValidationError) as e:
        check_password_strengh(None, field)

    assert_equal(e.exception.args[0], "Weak password: Missing at least 1 digit")


def test_check_password_strengh_at_least_one_uppercase():
    field = FakeField("longenoughpasswordbutnouppercase78")
    with assert_raises(ValidationError) as e:
        check_password_strengh(None, field)

    assert_equal(e.exception.args[0], "Weak password: Missing at least 1 uppercase character")


def test_check_password_strengh_at_least_one_lowercase():
    field = FakeField("LONGENOUGHPASSWORDBUTNOLOWERCASE78")
    with assert_raises(ValidationError) as e:
        check_password_strengh(None, field)

    assert_equal(e.exception.args[0], "Weak password: Missing at least 1 lowercase character")


def test_check_password_strengh_at_least_one_special_symbol():
    field = FakeField("LongEnoughP4ssW0rdButN0Speci4l")
    with assert_raises(ValidationError) as e:
        check_password_strengh(None, field)

    assert_equal(e.exception.args[0], "Weak password: Missing at least 1 special symbol (eg. !@#$%^&*.)")


def test_check_password_strengh_ok():
    field = FakeField("aSpecialPassword2018!")
    try:
        check_password_strengh(None, field)
    except Exception as e:
        raise e
    else:
        pass


def test_validate_email_exists_unknown_email():
    field = FakeField(random_email)
    with assert_raises(ValidationError) as e:
        validate_email_exists(None, field)
    assert_equal(e.exception.args[0], "Unknown Email")


def test_validate_email_exists_email_exists():
    user = create_user(random_email, "ASFGrehghaergbDAFBHEdbdebE211!", "public")
    field = FakeField(random_email)
    validate_email_exists(None, field)
    user.delete_instance()
    pass


def test_validate_is_email_available_email_taken():
    pass
    user = create_user(random_email, "ASFGrehghaergbDAFBHEdbdebE211!", "public")

    field = FakeField(random_email)
    with assert_raises(ValidationError) as e:
        validate_is_email_available(None, field)
    user.delete_instance()
    assert_equal(e.exception.args[0], "Email taken.")


def test_validate_is_email_available_no_email():
    field = FakeField("")
    with assert_raises(ValidationError) as e:
        validate_is_email_available(None, field)
    assert_equal(e.exception.args[0], "Field required.")


def test_validate_is_email_available_email_free():
    field = FakeField(random_email)
    validate_is_email_available(None, field)
    pass


def test_validate_valid_email_too_small():
    field = FakeField("XS@x.x")
    with assert_raises(ValidationError) as e:
        validate_valid_email(None, field)
    assert_equal(e.exception.args[0], "Sorry, this email adress is not valid.")


def test_validate_valid_email_missing_end():
    field = FakeField("xxx@xxx")
    with assert_raises(ValidationError) as e:
        validate_valid_email(None, field)
    assert_equal(e.exception.args[0], "Sorry, this email adress is not valid.")


def test_validate_valid_email_missing_at():
    field = FakeField("xxxxxx.com")
    with assert_raises(ValidationError) as e:
        validate_valid_email(None, field)
    assert_equal(e.exception.args[0], "Sorry, this email adress is not valid.")
