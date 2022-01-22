import os
from flask import Flask, render_template
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=os.getenv('SECRET_KEY'))


from app.lib.database import Initializer
initializer = Initializer()


from app.lib.authentication import login_required


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

''' Import and Register Blueprints '''

from app.modules.auth import auth_bp
app.register_blueprint(auth_bp)

from app.modules.brands import brands_bp
app.register_blueprint(brands_bp)

from app.modules.categories import categories_bp
app.register_blueprint(categories_bp)