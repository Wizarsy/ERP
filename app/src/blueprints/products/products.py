from flask import Blueprint
from .views.views import *


bp = Blueprint('products', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/products')

