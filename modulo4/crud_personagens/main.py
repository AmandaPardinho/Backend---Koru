from flask import Flask, render_template
import repositorio

app = Flask(__name__)

@app.route("/")
def home():
    dicionario = repositorio.retornarPersonagens()
    return render_template("index.html", dados = dicionario)

@app.route("/personagem/<int:id>")
def editar_personagem(id):

    # retorna os dados de um personagem na página de cadastro
    personagem = repositorio.retornarPersonagem(id)
    personagem['id'] = id
    return render_template("cadastro.html", **personagem)

app.run(debug = True)