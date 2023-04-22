class Mentor:
    # Método que define o objeto mentor
    def __init__(self, nome: str, linkedin: str, id = None):
        self.id = id
        self.nome = nome
        self.linkedin = linkedin

    # Método que precisa do objeto mentor já criado aqui no python
        # Retorna os valores guardados no objeto mentor em forma de dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "linkedin": self.linkedin
        }