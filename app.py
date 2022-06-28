import sqlite3

from sqlalchemy import true

con = sqlite3.connect("Itens_e_Valor_mercado.db")

cur = con.cursor()

#cur.execute('''CREATE TABLE itens_valores (item text, valor float)''')

#cur.execute("INSERT INTO itens_valores VALUES ('Arroz', 23.79)")

nome_item = input("Digite o nome do produto que será adicionado no Banco de Dados (Cuidado para não digitar um número!): ")

valor_item = input(f"Digite o valor do produto {nome_item}: ")

cur.execute("INSERT INTO itens_valores VALUES ('"+nome_item+"', "+valor_item+")")

cur.execute('''SELECT * FROM itens_valores ''')
print(cur.fetchall())

con.commit()
