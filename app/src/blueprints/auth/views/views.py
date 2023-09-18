from flask import flash, redirect, render_template, request, session, url_for
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash
from src.db import db

class loginView(MethodView):
  def get(self):
    return render_template('public/login.html')
  
  def post(self):
    login = request.form['login']
    passw = request.form['passw']
    error = None
    with db.connection() as conn:
      user = conn.execute("SELECT * FROM users WHERE email = %s OR username = %s", (login, login)).fetchone()
    if user is None:
      error = 'Incorrect Username'
    elif not check_password_hash(user['passwh'], passw):
      error = 'Incorrect Password'
    if error is None:
      session.clear()
      session['user_id'] = user['id']
      session.permanent = True
      return redirect(url_for('home.index'))
    flash(error)
    return redirect(url_for('auth.login'))

  
class registerView(MethodView):
  def get(self):
    return render_template('public/register.html')
  
  def post(self):
    username = request.form['username']
    email = request.form['email']
    passw = request.form['passw']
    error = None
    if not username:
      error = 'Username is required.'
    elif not email:
      error = 'email is required.'
    elif not passw:
      error = 'Password is required.'
    if error is None:
      with db.connection() as conn:
        try:
          conn.execute("INSERT INTO users (username, email, passwh) VALUES (%s, %s, %s)", (username, email, generate_password_hash(passw)))
        except conn.IntegrityError:
          error = f"User {username} is already registered."
        else:
           return redirect(url_for('auth.login'))
    flash(error)
    return redirect(url_for('auth.register'))
      
class logoutView(MethodView):
  def get(self):
    session.clear()
    return redirect(url_for('home.index'))