import sqlite3
from time import sleep

con = sqlite3.connect("Itens_e_Valor_mercado.db")

cur = con.cursor()

#cur.execute('''CREATE TABLE itens_valores (item text, valor float)''')

#cur.execute("INSERT INTO itens_valores VALUES ('Arroz', 23.79)")

def main():
    while True:
        dashboard()

def dashboard():
    print("""
    =================================
            Automação Mercado
    =================================
    """)
    option = input("""
    O que você deseja fazer?: 
    1) Adicioner item
    2) Mudar item
    3) Deletar item
    4) Mostrar dados do banco de dados
    5) Caucular desconto
    6) Finalizar expediente
    """)

    if option == '1' :
        add_item()
    elif option == '2' :
        mudar_item()
    elif option == '3' :
        deletar_item()
    elif option == '4' :
        mostrar_dado_na_tela()
    elif option == '5' :
        desconto()
    elif option == '6' :
        finalizar()

def add_item():
    nome_item = input("Digite o nome do produto que será adicionado no Banco de Dados (Cuidado para não digitar um número!): ")

    valor_item = input(f"Digite o valor do produto {nome_item}: ")

    cur.execute("INSERT INTO itens_valores VALUES ('"+nome_item+"', "+valor_item+")")

def mudar_item():
    pass

def deletar_item():
    pass

def mostrar_dado_na_tela():
    cur.execute('''SELECT * FROM itens_valores ''')
    print(cur.fetchall())

def desconto():
    valor = input("")

def finalizar():
    print("Finalizando...")
    sleep(5)

con.commit()

mostrar_dado_na_tela()
