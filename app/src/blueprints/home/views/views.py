from flask import g, render_template
from flask.views import MethodView

class homeView(MethodView):
  def get(self):
    return render_template('public/home.html')