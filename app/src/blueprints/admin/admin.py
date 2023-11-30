from flask import Blueprint
from .views.views import *

bp = Blueprint('admin', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/admin')


bp.add_url_rule('/', 'index', indexView.as_view('index'))