from flask import render_template
from flask.views import MethodView


class loginView(MethodView):
  def get(self):
    return render_template('public/login.html')