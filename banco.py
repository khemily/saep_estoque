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
    cursor = conexao.cursor()
    
    sql = """
    INSERT INTO produtos (nome, categoria, quantidade, preco)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nome, categoria, quantidade, preco)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
def lista_produto():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, categoria, quantidade, preco FROM produto")
    produto = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produto

def deletar_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM produtos WHERE id = %s"
    cursor.execute(sql, (id_produto,))
   
    conexao.commit()

    cursor.close()
    conexao.close()