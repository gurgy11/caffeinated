from flask import Blueprint, redirect, render_template, session, request, url_for, jsonify
from app.lib.authentication import login_required


bp = Blueprint('brands', __name__, url_prefix='/brands')


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('brands/index.html', title='Brands')