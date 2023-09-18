from flask import Blueprint, render_template

bp = Blueprint('error', __name__, static_folder = 'static', template_folder = 'templates')


@bp.app_errorhandler(404)
def pageNotFound(error):
  return render_template('public/pageNotFound.html'), 404