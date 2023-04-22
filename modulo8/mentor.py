import sqlite3

class Mentor:
    # Método que define o objeto mentor
    def __init__(self, nome: str, linkedin: str, id = None):
        self.id = id
        self.nome = nome
        self.linkedin = linkedin

    # Sempre que a palavra 'self' aparecer dentro do parênteses do método => é um método que precisa do objeto mentor já criado aqui no python
        # Retorna os valores guardados no objeto mentor em forma de dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "linkedin": self.linkedin
        }
    
    # Método que cria um novo mentor no banco de dados caso não haja id ou método que atualiza dados de um mentor caso haja id
    def save(self, db_connection: sqlite3.Connection):
        if self.id is None:
            query = "INSERT INTO mentores (nome_mentor, linkedin_mentor) VALUES (?, ?)"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.nome, self.linkedin))
            self.id = cursor.lastrowid
            # self.id = db_connection.execute(query, (self.nome, self.linkedin))
        else:
            query = "UPDATE mentores SET nome_mentor = ?, linkedin_mentor = ? WHERE id_mentor = ?"
            db_connection.execute(query, (self.nome, self.linkedin, self.id))
        db_connection.commit()
        db_connection.close()
