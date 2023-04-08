# Dicionário com dados fornecidos pelo programador

dicionario = {
    "nome": "Amanda",
    "altura": 1.68,
    "profissão": "Desenvolvedora, Acupunturista"
}

print(dicionario)


# Dicionário com dados fornecidos pelo usuário
    # Criação de uma função genérica


def retornarProduto(dicionario):
    textoSaida = f"Nome: {dicionario['nome']}\nDescrição: {dicionario['descrição']}\nPeso: {dicionario['peso']}" \
                 f"\nPreço: {dicionario['preço']}\nLançamento: {dicionario['lançamento']}"
    return textoSaida

produto = {}

# Coleta de dados informados pelo usuário
produto["nome"] = input("Informe o nome do produto: ")
produto["descrição"] = input("Informe a descrição do produto: ")
produto["lançamento"] = int(input("Informe o ano de lançamento do produto: "))
produto["preço"] = float(input("Informe o valor do produto em reais: "))
produto["peso"] = float(input("Informe o peso do produto em quilogramas: "))

print(produto)

for chave, valor in produto.items():
    print(f"{chave} - {valor}")

print(retornarProduto(produto))
