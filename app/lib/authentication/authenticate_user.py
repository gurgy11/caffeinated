import functools
from flask import session, redirect, url_for


def login_required(view):
    @functools.wraps(view)
    def authenticate(*args, **kwargs):
        if 'user_id' not in session:
            print('User is not authenticated and has been redirected to the login page.')
            return redirect(url_for('auth.login'))
        else:
            return view(*args, **kwargs)
    return authenticate