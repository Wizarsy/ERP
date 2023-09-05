from flask import Flask
import src.db as db

app = Flask(__name__)

app.add_url_rule()
# @app.get("/")
# def login():
#     return render_template('login.html')

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