from flask import Blueprint, render_template, abort

bp = Blueprint('home', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/')

@bp.route('/home')
@bp.route('/')
def index():
  return 'home'


@bp.app_errorhandler(404)
def pageNotFound(error):
  return 'Page not Found', 404
