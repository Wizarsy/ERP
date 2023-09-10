from flask import Blueprint
from .views import views

bp = Blueprint('admin', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/admin')


bp.add_url_rule('/', view_func = views.index.as_view('index'))