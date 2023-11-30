from flask import Flask
from src.config import CONFIG

from .blueprints.admin import admin
from .blueprints.auth import auth
from .blueprints.dashboard import dashboard
from .blueprints.error import error
from .blueprints.home import home

app = Flask(__name__)
app.config.update(**CONFIG['flask'])

app.register_blueprint(home.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(dashboard.bp)
app.register_blueprint(error.bp)