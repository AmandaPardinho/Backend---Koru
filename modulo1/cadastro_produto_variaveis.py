def exibirProduto():
      print(f"Nome: {nomeProduto}\nDescrição: {descricaoProduto}\nPeso: {pesoProduto}\nPreço: {valorProduto}\n"
            f"Lançamento: {anoLancamentoProduto}")

def retornaProduto():
      textoSaida = f"Nome: {nomeProduto}\nDescrição: {descricaoProduto}\nPeso: {pesoProduto}\nPreço: {valorProduto}\n"
      f"Lançamento: {anoLancamentoProduto}"
      return textoSaida

print("CADASTRO DE PRODUTOS")

# Iniciando a coleta de dados informados pelo usuário
nomeProduto = input("Por favor, informe o nome do produto: ")
descricaoProduto = input("Por favor, informe a descrição do produto: ")
anoLancamentoProduto = int(input("Por favor, informe o ano de lançamento do produto: "))
valorProduto = float(input("Por favor, informe o valor do produto em reais: "))
pesoProduto = float(input("Por favor, informe o peso do produto em kg: "))

# Exibição simples do produto
print(nomeProduto)
print(descricaoProduto)
print(anoLancamentoProduto)
print(valorProduto)
print(pesoProduto)

# Exibição das variáveis usando texto
print(f"Nome: {nomeProduto}\nDescrição: {descricaoProduto}\nPeso: {pesoProduto}\nPreço: {valorProduto}\nLançamento: "
      f"{anoLancamentoProduto}\n")

exibirProduto()

print(retornaProduto())