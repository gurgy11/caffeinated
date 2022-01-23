import functools
from flask import session, redirect, url_for


def login_required(view):
    @functools.wraps(view)
    def authenticate(*args, **kwargs):
        if 'user_id' not in session or 'user_username' not in session:
            print('User is not authenticated and has been redirected to the login page.')
            return redirect(url_for('auth.login'))
        else:
            return view(*args, **kwargs)
    return authenticate

def set_user_session(user_id, username):
    ''' Sets the user in the session, authenticating them '''
    
    session['user_id'] = user_id
    session['user_username'] = username
    
    print('User session created for user {username} with id {user_id}.'.format(username=username, user_id=user_id))

def unset_user_session():
    ''' Clears the session variable, making the user unauthenticated '''
    
    session.clear()
    
    print('User session cleared and returned to login.')