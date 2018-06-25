from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user


def confirmed_required(func):
    """
    This will check if the function what is decorated with this has a
    user with a confirmed email
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """
        The decorated function
        """
        if current_user.is_confirmed is False:
            flash('Please confirm your account!', 'warning')
            return redirect(url_for('unconfirmed'))
        return func(*args, **kwargs)

    return decorated_function


def admin_only(func):
    """
    This will check if the function what is decorated with this has
    a admin user.
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """
        The decorated function
        """
        if current_user.scope != "admin":
            flash('Sorry, but you don\'t have access to this page', 'warning')
            return redirect(url_for('home'))
        return func(*args, **kwargs)

    return decorated_function
