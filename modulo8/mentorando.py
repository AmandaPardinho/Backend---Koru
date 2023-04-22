import sqlite3

class Mentorando:
    def __init__(self, nome: str, linkedin: str, id = None):
        self.id = id
        self.nome = nome
        self.linkedin = linkedin

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "linkedin": self.linkedin
        }
    
    # Este método da classe Mentorandos possui novamente o 'cursor', pois será necessário chamar o lastrowid e isso só é possível com ele presente
    def save(self, db_connection: sqlite3.Connection):
        if self.id is None:
            query = "INSERT INTO mentorandos (nome_mentorando, linkedin_mentorando) VALUES (?, ?)"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.nome, self.linkedin))
            self.id = cursor.lastrowid
        else:
            query = "UPDATE mentorandos SET nome_mentorando = ?, linkedin_mentorando = ? WHERE id_mentorando = ?"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.nome, self.linkedin, self.id))
        db_connection.commit()
        db_connection.close()