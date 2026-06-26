import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from banco import cadastrar_produto, lista_produto

janela = tk.Tk ()
janela.title("SAEP Estoque Fácil")
janela.geometry("500x400")

tabela = ttk.Treeview(
     janela,
     columns=("id", "nome", "categoria", "quantidade", "preco"), 
     show="headings"
)

tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("categoria", text="Categoria")
tabela.heading("quantidade", text="Qtd")
tabela.heading("preco", text="Preço")

tabela.column("id", width=50)
tabela.column("nome", width=160)
tabela.column("categoria", width=140)
tabela.column("quantidade", width=80)
tabela.column("preco", width=80)

tabela.pack(pady=10)

def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)

    produtos = lista_produto()
    for produto in produtos:
        tabela.insert("", tk.END, values=produto)

atualizar_tabela()

título = tk.Label(
    janela,
    text="SAEP Estoque Fácil",
    font=("Arial", 18, "bold")
)
título.pack(pady=10)

tk.Label(janela, text="Nome do Produto:").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="Categoria:").pack()
entrada_categoria = tk.Entry(janela, width=40)
entrada_categoria.pack()

tk.Label(janela, text="Quantidade:").pack()
entrada_quantidade = tk.Entry(janela, width=40)
entrada_quantidade.pack()

tk.Label(janela, text="Preço:").pack()
entrada_preco = tk.Entry(janela, width=40)
entrada_preco.pack()

def salvar():
    nome = entrada_nome.get()
    categoria = entrada_categoria.get()
    quantidade = entrada_quantidade.get()
    preco = entrada_preco.get()

    if nome == "" or categoria == "" or quantidade == "" or preco == "":
         messagebox.showwarning("Atenção", "preencha todos os campos.")
         return
    cadastrar_produto(nome, categoria,int(quantidade), float(preco))  
    messagebox.showinfo("sucesso", "produto cadastrado com sucesso!")

    entrada_nome.delete(0, tk.END)
    entrada_categoria.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)

botao_salvar = tk.Button(
         janela,
         text="Cadastrar Produto",
         command=salvar,
         width=25
    )
botao_salvar.pack (pady=20)

janela.mainloop()

cadastrar_produto(nome, categoria, int(quantidade), float(preco))

messagebox.showinfo("sucesso", "produto cadastrado com sucesso!")

entrada_nome.delete(0, tk.END)
entrada_categoria.delete(0, tk.END)
entrada_quantidade.delete(0, tk.END)
entrada_preco.delete(0, tk.END)

atualizar_tabela()