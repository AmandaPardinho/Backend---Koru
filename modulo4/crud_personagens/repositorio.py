personagens = {
    1: {
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d7/Harry_Potter_character_poster.jpg"
    },
    2: {
        "nome": "Ron Weasley",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "01/03/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5e/Pon_Weasley_poster.jpg"
    },
    3: {
        "nome": "Hermione Granger",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.65,
        "nascimento": "19/09/1979",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d3/Hermione_Granger_poster.jpg"
    },
    4: {
        "nome": "Draco Malfoy",
        "raca": "Humano",
        "casa": "Sonserina",
        "altura": 1.80,
        "nascimento": "05/06/1980",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/1/16/Draco_Mal.JPG"
    }
}

def gerarId():
    id = len(personagens) + 1
    return id

def criarPersonagem(nome, raca, casa, altura, nascimento, imagem):
    personagens[gerarId()] = {"nome": nome, "raca": raca, "casa": casa, "altura": altura, "nascimento": nascimento, "imagem": imagem}

def retornarPersonagens():
    return personagens

print(retornarPersonagens())

criarPersonagem("Amanda", "Humano", "Grifinória", 1.68, "03/01/1989", "")

print(retornarPersonagens())