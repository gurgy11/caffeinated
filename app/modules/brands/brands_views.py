from flask import Blueprint, redirect, render_template, session, request, url_for, jsonify
from app.lib.authentication import login_required
from .brands_controller import BrandsController


bp = Blueprint('brands', __name__, url_prefix='/brands')
ROWS_PER_PAGE = 5


@bp.route('/index/<int:page>')
@login_required
def index(page=None):
    controller = BrandsController()
    num_pages = controller.num_pages(ROWS_PER_PAGE)
    return render_template('brands/index.html', title='Brands', num_pages=num_pages, page=page)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    ''' Handles the create brand form '''
    
    if request.method == 'POST':
        controller = BrandsController()
        if controller.create(request.form):
            return redirect(url_for('brands.index', page=1))
        else:
            errors = controller.errors
            return render_template('brands/create.html', title='Create Brand', errors=errors)
    
    return render_template('brands/create.html', title='Create Brand')


@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    brand_id = id
    
    controller = BrandsController()
    controller.delete(brand_id)
    
    return redirect(url_for('brands.index', page=1))


@bp.route('/fetch_all')
@login_required
def fetch_all():
    ''' Fetches all brands as JSON '''
    
    controller = BrandsController()
    brands = controller.fetch_all()
    
    return jsonify(brands)


@bp.route('/fetch/<int:page>')
@login_required
def fetch(page):
    controller = BrandsController()
    brands = controller.fetch(page, ROWS_PER_PAGE)
    return jsonify(brands)

@bp.route('/num_pages')
@login_required
def num_pages():
    controller = BrandsController()
    num_pages = controller.num_pages()
    json_pages = {'num_pages': num_pages}
    return jsonify(json_pages)