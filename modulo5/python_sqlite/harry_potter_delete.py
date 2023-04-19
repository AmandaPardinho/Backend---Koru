import sqlite3

#Conectar com o banco de dados
conexao = sqlite3.connect('harry_potter_personagens.db')

# Deletando informação do banco de dados
cursor = conexao.cursor()
sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_delete, (4, ))
conexao.commit()
sql_select_unico = "SELECT * FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_select_unico, (4, ))
print(cursor.fetchone())