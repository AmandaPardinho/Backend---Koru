import sqlite3

#Conectar com o banco de dados
conexao = sqlite3.connect('harry_potter_personagens.db')

# Atualizando um personagem
cursor = conexao.cursor()
sql_update = "UPDATE personagens SET nome_personagem = ? WHERE id_personagem = ?"
cursor.execute(sql_update, ("Ron Weasley", 2))
conexao.commit()
sql_select_unico = "SELECT * FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_select_unico, (2, ))
print(cursor.fetchone())