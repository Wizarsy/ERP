from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
  teste = request.args.get("token")
  print(teste)
  return {"r": teste}



app.run(debug=True)