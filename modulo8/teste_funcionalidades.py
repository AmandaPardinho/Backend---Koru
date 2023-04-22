from mentor import Mentor
from mentorando import Mentorando
from mentoria import Mentoria
from db_connector import DBConnector

db = DBConnector("mentorias.db")

# Teste novo mentor
novo_mentor = Mentor("Thor", "https://siteteste/thor")
novo_mentor.save(db.connect())
print(novo_mentor.to_dict())

# Teste novo mentorando
novo_mentorando = Mentorando("Batman", "https://siteteste/batman")
novo_mentorando.save(db.connect())
print(novo_mentorando.to_dict())

# Teste nova mentoria
nova_mentoria = Mentoria(novo_mentor, novo_mentorando, "2023-04-22")
nova_mentoria.save(db.connect())
print(nova_mentoria.to_dict())