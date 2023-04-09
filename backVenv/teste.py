from flask import Flask

app = Flask(__name__)

@app.route("/")
def testeFlask():
    return "<h1>O venv funcionou!!!!</h1>"

app.run(debug=True)
