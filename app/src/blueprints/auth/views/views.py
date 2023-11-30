from flask import abort, flash, g, redirect, render_template, request, session, url_for
from flask.views import MethodView
from psycopg.errors import UniqueViolation
from src.db import db
from src.services.auth_token import decodeToken, encodeToken
from src.services.email_tools import sendEmail
from werkzeug.security import check_password_hash, generate_password_hash


class loginView(MethodView):
  def get(self):
    return render_template("public/login.html")
  
  def post(self):
    user_login = request.form["login"] or request.args.get("login")
    user_passw = request.form["passw"] or request.args.get("passw")
    error = None
    with db.connection() as dq:
      user = dq.execute("SELECT * FROM users_account WHERE email = %s OR username = %s", (user_login, user_login)).fetchone()
    if user is None or not check_password_hash(user["passwh"], user_passw):
      error = "Incorrect Username or Password"
    elif not user["email_confirmed"]:
      return redirect(url_for("auth.activeAccount", user = user["id"]))
    if error is None:
      session.clear()
      session["user_id"] = user["id"]
      session.permanent = True
      return redirect(url_for("home.index"))
    flash(error)
    return redirect(url_for("auth.login"))


class registerView(MethodView):
  def get(self):
    return render_template("public/register.html")
  
  def post(self):
    user_name = request.form["name"]
    user_email = request.form["email"]
    user_confirm_email = request.form["confirm_email"]
    user_passw = request.form["passw"]
    user_confirm_passw = request.form["confirm_passw"]
    error = None
    if not user_name:
      error = "Username is required."
    elif not user_email:
      error = "email is required."
    elif not user_passw:
      error = "Password is required."
    elif user_email != user_confirm_email:
      error = "E-mail do not match"
    elif user_passw != user_confirm_passw:
      error = "Passwords do not match"
    if error is None:
      with db.connection() as dq:
        with dq.transaction():
          try:
            dq.execute("INSERT INTO users_account (username, email, passwh) VALUES (%s, %s, %s)", (user_name, user_email, generate_password_hash(user_passw)))
          except UniqueViolation:
            flash(f"User {user_name} is already registered.")
            return redirect(url_for("auth.register"))
        user = dq.execute("SELECT * FROM users_account WHERE email = %s", [user_email]).fetchone()
      return redirect(url_for("auth.activeAccount", user = user["id"]))
    flash(error)
    return redirect(url_for("auth.register"))

      
class logoutView(MethodView):
  def get(self):
    session.clear()
    return redirect(url_for("home.index"))


class activeAccountView(MethodView):
  def get(self):
    token = request.args.get("token")
    user_id = request.args.get("user")
    if token is not None:
      dec_token = decodeToken(token, "activeAccount")
      with db.connection() as dq:
        user = dq.execute("SELECT * FROM users_account WHERE id = %s", [dec_token["info"]]).fetchone()
      if dec_token["status"] and not user["email_confirmed"]:
        with db.connection() as dq:
          with dq.transaction():
            dq.execute("UPDATE users_account SET email_confirmed = True WHERE id = %s", [dec_token["info"]])
        flash("Your account has been verified", "success")
        return redirect(url_for("auth.login"))
      elif not dec_token["status"]:
        flash(dec_token["info"], "error")
        return redirect(url_for("auth.login"))
      else:
        return redirect(url_for("home.index"))
    elif user_id:
      with db.connection() as dq:
        user = dq.execute("SELECT * FROM users_account WHERE id = %s", [user_id]).fetchone()
      enc_token = encodeToken(user["id"], "activeAccount")
      sendEmail(user["email"], "Active account", url_for("auth.activeAccount", token = enc_token, _external = True))
      return render_template("public/active_account.html")
    else:
      return redirect(url_for("auth.login"))
    
  def post(self):
    user = request.args.get("user")
    return redirect(url_for("auth.activeAccount", user = user))
  
  
class forgotPasswordView(MethodView):
  def get(self):
    token = request.args.get("token")
    if token is not None:
      dec_token = decodeToken(token, "forgotPassword")
      if dec_token["status"]:
        return render_template("public/reset_password.html")
      else:
        flash(dec_token["info"], "error")
        return redirect(url_for("auth.login"))
    else:
      return render_template("public/forgot_password.html")
  
  def post(self):
    token = request.args.get("token")
    if token is not None:
      dec_token = decodeToken(token, "forgotPassword")
      if dec_token["status"]:
        user_new_passw = request.form["new_passw"]
        user_confirm_new_passw = request.form["confirm_new_passw"]
        error = None
        with db.connection() as dq:
          user = dq.execute("SELECT * FROM users_account WHERE id = %s", [dec_token["info"]]).fetchone()
        if not user_new_passw:
          error = "You need to provide a password"
        elif not user_confirm_new_passw:
          error = "You need to confirm the password"
        elif user_new_passw != user_confirm_new_passw:
          error = "Passwords do not match"
        elif check_password_hash(user["passwh"], user_new_passw):
          error = "The password cannot be the same"
        if error is None:
          with db.connection() as dq:
            with dq.transaction():
              dq.execute("UPDATE users_account SET passwh = %s WHERE id = %s", (generate_password_hash(user_new_passw), user["id"]))
          flash("Password updated", "success")
          return redirect(url_for("auth.login"))
        else:
          flash(error, "error")
          return redirect(url_for("auth.forgotPassword", token = token))
      else:
        flash(dec_token["info"], "error")
        return redirect(url_for("auth.login"))
    else:
      user_email = request.form["email"]
      error = None
      if not user_email:
        error = "You need to provide a email"
      if error is None:
        with db.connection() as dq:
          user = dq.execute("SELECT * FROM users_account WHERE email = %s", [user_email]).fetchone()
        if user is not None:
          enc_token = encodeToken(user["id"], "forgotPassword")
          try:
            sendEmail(user["email"], "Reset password", url_for("auth.forgotPassword", token = enc_token, _external = True))
          except:
            abort(500)
          flash("Check your email for a link to reset your password.", "success")
          return redirect(url_for("auth.login"))
        else:
          flash("User not found", "error")
          return redirect(url_for("auth.forgotPassword"))
      else:
        flash(error, "error")
        return redirect(url_for("auth.forgotPassword")) 
