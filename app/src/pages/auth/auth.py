from flask import Blueprint, redirect, render_template, request, url_for
from .views import views

bp = Blueprint('auth', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/auth')

# @bp.before_app_request
# def checkAuth():
#   if request.endpoint != 'auth.login':
#     return redirect(url_for('auth.login'))  
bp.add_url_rule('/login', view_func = views.loginView.as_view('login'))
