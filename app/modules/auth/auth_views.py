import functools
from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from .auth_controller import AuthController


bp = Blueprint('auth', __name__, url_prefix='/auth')
controller = AuthController()


@bp.route('/register', methods=['GET', 'POST'])
def register():
    ''' Handles the user registration form '''
    
    if request.method == 'POST':
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
        return jsonify(request.form)
    
    return render_template('auth/login.html', title='Login')