import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from banco import cadastrar_produto, listar_produtos, excluir_produto


janela = tk.Tk()
janela.title("SAEP Estoque Fácil")
janela.geometry("760x560")
janela.configure(bg="#f4f6f8")


titulo = tk.Label(
    janela,
    text="SAEP Estoque Fácil",
    font=("Arial", 20, "bold"),
    bg="#f4f6f8",
    fg="#164193"
)
titulo.pack(pady=10)


subtitulo = tk.Label(
    janela,
    text="Cadastro, listagem e exclusão de produtos",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#575756"
)
subtitulo.pack(pady=2)


def criar_label(texto):
    label = tk.Label(
        janela,
        text=texto,
        bg="#f4f6f8",
        fg="#111827",
        font=("Arial", 10, "bold")
    )
    label.pack()


criar_label("Nome do produto:")
entrada_nome = tk.Entry(janela, width=42)
entrada_nome.pack(pady=2)

criar_label("Categoria:")
entrada_categoria = tk.Entry(janela, width=42)
entrada_categoria.pack(pady=2)

criar_label("Quantidade:")
entrada_quantidade = tk.Entry(janela, width=42)
entrada_quantidade.pack(pady=2)

criar_label("Preço:")
entrada_preco = tk.Entry(janela, width=42)
entrada_preco.pack(pady=2)


def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_categoria.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)


def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)

    produtos = listar_produtos()

    for produto in produtos:
        tabela.insert("", tk.END, values=produto)


def salvar():
    nome = entrada_nome.get().strip()
    categoria = entrada_categoria.get().strip()
    quantidade = entrada_quantidade.get().strip()
    preco = entrada_preco.get().strip()

    if nome == "" or categoria == "" or quantidade == "" or preco == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    try:
        quantidade = int(quantidade)
        preco = float(preco)
    except ValueError:
        messagebox.showwarning(
            "Atenção",
            "Quantidade deve ser número inteiro e preço deve usar ponto. Exemplo: 2.50"
        )
        return

    if quantidade < 0:
        messagebox.showwarning(
            "Atenção",
            "A quantidade não pode ser negativa."
        )
        return

    if preco <= 0:
        messagebox.showwarning(
            "Atenção",
            "O preço deve ser maior que zero."
        )
        return

    cadastrar_produto(nome, categoria, quantidade, preco)

    messagebox.showinfo(
        "Sucesso",
        "Produto cadastrado com sucesso!"
    )

    limpar_campos()
    atualizar_tabela()


def excluir():
    item_selecionado = tabela.selection()

    if not item_selecionado:
        messagebox.showwarning(
            "Atenção",
            "Selecione um produto para excluir."
        )
        return

    item = tabela.item(item_selecionado)
    id_produto = item["values"][0]

    resposta = messagebox.askyesno(
        "Confirmar exclusão",
        "Deseja realmente excluir o produto selecionado?"
    )

    if resposta:
        excluir_produto(id_produto)
        atualizar_tabela()

        messagebox.showinfo(
            "Sucesso",
            "Produto excluído com sucesso!"
        )


frame_botoes = tk.Frame(janela, bg="#f4f6f8")
frame_botoes.pack(pady=10)

botao_salvar = tk.Button(
    frame_botoes,
    text="Cadastrar Produto",
    command=salvar,
    width=20,
    bg="#164193",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_salvar.grid(row=0, column=0, padx=5)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar Campos",
    command=limpar_campos,
    width=20
)
botao_limpar.grid(row=0, column=1, padx=5)

botao_excluir = tk.Button(
    frame_botoes,
    text="Excluir Produto",
    command=excluir,
    width=20,
    bg="#e7490f",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_excluir.grid(row=0, column=2, padx=5)


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
tabela.column("nome", width=180)
tabela.column("categoria", width=160)
tabela.column("quantidade", width=80)
tabela.column("preco", width=100)

tabela.pack(pady=10)

atualizar_tabela()

janela.mainloop()