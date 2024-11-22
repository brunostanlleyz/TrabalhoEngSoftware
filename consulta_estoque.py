import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Função para consultar componentes no banco de dados
def consultar_componentes(filtro, valor):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        if filtro == "Código":
            query = "SELECT nome, codigo, fabricante, categoria, quantidade FROM componentes WHERE codigo LIKE ?"
        elif filtro == "Nome":
            query = "SELECT nome, codigo, fabricante, categoria, quantidade FROM componentes WHERE nome LIKE ?"
        elif filtro == "Categoria":
            query = "SELECT nome, codigo, fabricante, categoria, quantidade FROM componentes WHERE categoria LIKE ?"
        else:
            query = "SELECT nome, codigo, fabricante, categoria, quantidade FROM componentes"

        cursor.execute(query, (f"%{valor}%",) if filtro in ["Código", "Nome", "Categoria"] else ())
        resultados = cursor.fetchall()
        conn.close()
        return resultados

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar estoque: {e}")
        return []

# Função para criar a interface de consulta de estoque
def consulta_estoque(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    title = tk.Label(content_frame, text="Consulta de Estoque em Tempo Real", font=("Arial", 14))
    title.pack(pady=10)

    # Frame de Filtros de Pesquisa
    filtro_frame = tk.Frame(content_frame)
    filtro_frame.pack(pady=5)

    lbl_filtro = tk.Label(filtro_frame, text="Filtrar por:", width=15)
    lbl_filtro.pack(side=tk.LEFT)

    filtro_opcoes = ["Todos", "Código", "Nome", "Categoria"]
    filtro_var = tk.StringVar(value=filtro_opcoes[0])
    filtro_menu = ttk.Combobox(filtro_frame, textvariable=filtro_var, values=filtro_opcoes, width=20)
    filtro_menu.pack(side=tk.LEFT, padx=5)

    entry_pesquisa = tk.Entry(filtro_frame, width=40)
    entry_pesquisa.pack(side=tk.LEFT, padx=5)

    # Tabela de Resultados
    resultados_frame = tk.Frame(content_frame)
    resultados_frame.pack(pady=10)

    colunas = ["Nome", "Código", "Fabricante", "Categoria", "Quantidade"]
    tree = ttk.Treeview(resultados_frame, columns=colunas, show="headings", height=15)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(side=tk.LEFT)

    # Função para atualizar a tabela de resultados
    def atualizar_tabela():
        filtro = filtro_var.get()
        valor = entry_pesquisa.get()
        resultados = consultar_componentes(filtro, valor)

        # Limpar a tabela
        for item in tree.get_children():
            tree.delete(item)

        # Inserir novos dados
        for row in resultados:
            tree.insert("", tk.END, values=row)

    # Botão de pesquisa
    btn_pesquisar = tk.Button(filtro_frame, text="Pesquisar", command=atualizar_tabela)
    btn_pesquisar.pack(side=tk.LEFT, padx=5)

    # Atualizar a tabela ao abrir a tela
    atualizar_tabela()
