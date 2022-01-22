from flask import Blueprint, redirect, render_template, url_for, session, jsonify, request
from app.lib.authentication import login_required


bp = Blueprint('categories', __name__, url_prefix='/categories')


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('categories/index.html', title='Categories')