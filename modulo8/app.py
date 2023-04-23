from flask import Flask, request, jsonify
from mentor import Mentor
from mentorando import Mentorando
from mentoria import Mentoria
from db_connector import DBConnector

app = Flask(__name__)

db = DBConnector("mentorias.db")

# Retorna todos os mentores
@app.route("/mentores", methods = ['GET'])
def get_mentores():
    mentores = Mentor.get_all(db.connect())
    return jsonify(mentores)

# Retorna um único mentor pelo id
@app.route("/mentores/<int:id_mentor>", methods = ['GET'])
def get_mentor(id_mentor):
    mentor = Mentor.get_by_id(id_mentor, db.connect())
    if mentor:
        return jsonify(mentor.to_dict())
    else:
        return jsonify({"error": "Mentor não localizado"}), 404
    
# Retorna todos os mentorandos
@app.route("/mentorandos", methods = ['GET'])
def get_mentorandos():
    mentorandos = Mentorando.get_all(db.connect())
    return jsonify(mentorandos)

# Retorna um único mentorando
@app.route("/mentorandos/<int:id_mentorando>", methods = ['GET'])
def get_mentorando(id_mentorando):
    mentorando = Mentorando.get_by_id(id_mentorando, db.connect())
    if mentorando:
        return jsonify(mentorando.to_dict())
    else:
        return jsonify({"error": "Mentorando não localizado"}), 404

# Retorna todas as mentorias
@app.route("/mentorias", methods = ['GET'])
def get_mentorias():
    mentorias = Mentoria.get_all(db.connect())
    return jsonify(mentorias)

# Retorna uma única mentoria
@app.route("/mentorias/<int:id_mentoria>", methods = ['GET'])
def get_mentoria(id_mentoria):
    mentoria = Mentoria.get_by_id(id_mentoria, db.connect())
    if mentoria:
        return jsonify(mentoria.to_dict())
    else:
        return jsonify({"error": "Mentoria não localizada"}), 404

app.run(debug = True)