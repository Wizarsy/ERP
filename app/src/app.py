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


# @app.route("/resultado", methods = ['GET', 'POST'])
# def resultado():
#     if request.method == 'POST':
#         nome = request.form['nome']
#         email = request.form['email']
#         senha = request.form['senha']
#         cur.execute(f"""INSERT INTO Usuario (NOME, EMAIL, SENHA) VALUES
#         ('{nome}', '{email}', '{senha}')
#         """)
#         conn.commit()
#         return render_template('login.html')