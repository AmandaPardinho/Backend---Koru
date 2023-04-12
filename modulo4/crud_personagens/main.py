from flask import Flask, render_template
import repositorio

app = Flask(__name__)

@app.route("/")
def home():
    dicionario = repositorio.retornarPersonagens()
    return render_template("index.html", dados = dicionario)

app.run(debug = True)