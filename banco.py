import mysql.connector

def conectar ():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senai",
        database="saep_estoque"
    )
    return conexao

def cadastrar_produto(nome, categoria, quantidade, preco):
    conexao = conectar()
    cursor = conexao.curso()
    
    sql = """
    INSERT INTO produtos (nome, categoria, quantidade, preco)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nome, categoria, quantidade, preco)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
