from flask.views import MethodView
from src.middleware.login_required import loginRequired

class indexView(MethodView):
  
  decorators = [loginRequired]
  def get(self):
    return {'route': 'admin'}, 200