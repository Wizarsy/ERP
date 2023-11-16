from flask.views import MethodView
from src.middleware.login_required import loginRequired


class registerView(MethodView):
  decorators = [loginRequired]
  def get():
    return
  
  def post():
    return
  
class updateView(MethodView):
  decorators = [loginRequired]
  def get():
    return
  
  def post():
    return
  
class deleteView(MethodView):
  decorators = [loginRequired]
  def get():
    return
  
  def post():
    return
  