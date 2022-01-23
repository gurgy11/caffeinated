from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from .auth_controller import AuthController
from app.lib.authentication import set_user_session, unset_user_session


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    ''' Handles the user registration form '''
    
    if request.method == 'POST':
        controller = AuthController()
        if not controller.register(request.form):
            errors = controller.errors
            return render_template('auth/register.html', title='Register', errors=errors)
        else:
            return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Register')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    ''' Handles the user login form '''
    
    if request.method == 'POST':
        controller = AuthController()
        if not controller.login(request.form):
            print("Could not authenticate.")
            errors = controller.errors
            return render_template('auth/login.html', title='Login', errors=errors)
        else:
            print("User authenticated.")
            return redirect(url_for('index'))
    
    return render_template('auth/login.html', title='Login')


@bp.route('/logout')
def logout():
    ''' Handles the user logout request '''
    
    unset_user_session()
    return redirect(url_for('auth.login'))