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

from time import sleep

from nose.tools import assert_true, assert_false, assert_equal

from openapprentice.utils.email import is_valid_email, generate_confirmation_token, confirm_token
from openapprentice.utils.strings import get_random_string

random_email = get_random_string() + "@" + get_random_string() + ".com"


def test_is_valid_email():
    assert_true(is_valid_email(random_email))
    assert_false(is_valid_email(random_email[:-3]))


def test_token_gen_and_check_valid_token():
    token = generate_confirmation_token(random_email)
    assert_equal(random_email, confirm_token(token))


def test_token_gen_and_check_expired_token():
    token = generate_confirmation_token(random_email)
    sleep(2)
    resp = confirm_token(token, expiration=1)
    assert_false(resp)


def test_token_gen_and_check_missing_part_of_token():
    token = generate_confirmation_token(random_email)
    resp = confirm_token(token[:-5])
    assert_false(resp)
