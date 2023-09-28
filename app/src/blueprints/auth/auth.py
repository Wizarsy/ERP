from flask import Blueprint, g, redirect, render_template, request, session, url_for
from .views.views import *
from src.db import db

bp = Blueprint('auth', __name__, static_folder = 'static', template_folder = 'templates', url_prefix = '/auth')

@bp.before_app_request
def loadUser():
  user_id = session.get('user_id')
  if user_id is None:
   g.user = None
  else:
    with db.connection() as dq:
      g.user = dq.execute("SELECT * FROM users_account WHERE id = %s", [user_id]).fetchone()

bp.add_url_rule('/login', 'login', loginView.as_view('login'))
bp.add_url_rule('/register', 'register', registerView.as_view('register'))
bp.add_url_rule('/logout', 'logout', logoutView.as_view('logout'))
bp.add_url_rule('/active-account', 'activeAccount', activeAccountView.as_view('activeAccount'))
bp.add_url_rule('/forgot-password', 'forgotPassword', forgotPasswordView.as_view('forgotPassword'))