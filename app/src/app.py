from flask import Flask
from .pages.home import home
from .pages.auth import auth
from .pages.admin import admin
from .pages.dashboard import dashboard

app = Flask(__name__)


app.register_blueprint(home.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(dashboard.bp)


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