from flask import Blueprint, render_template


bp = Blueprint('dashboard', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/dashboard')

@bp.route('/')
def index():
  return 'dashboard'