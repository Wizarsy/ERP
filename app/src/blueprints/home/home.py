from flask import Blueprint
from .views.views import *

bp = Blueprint('home', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/')

bp.add_url_rule('/', 'index', homeView.as_view('index'))
bp.add_url_rule('/home', 'home', homeView.as_view('home'))