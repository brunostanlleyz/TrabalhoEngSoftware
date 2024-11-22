import tkinter as tk
from tkinter import ttk, messagebox
from utils import criar_usuario
import sqlite3

def cadastro_usuarios(content_frame):
    # Limpa o frame de conteúdo
    for widget in content_frame.winfo_children():
        widget.destroy()

    title = tk.Label(content_frame, text="Cadastro de Usuários", font=("Arial", 14))
    title.pack(pady=10)

    # Mensagem de status
    status_msg = tk.Label(content_frame, text="", font=("Arial", 12), fg="green")
    status_msg.pack(pady=5)

    # Formulário de Cadastro
    frame_form = tk.Frame(content_frame)
    frame_form.pack(pady=10)

    labels = ["Nome", "Usuário", "Senha"]
    entries = {}

    for label in labels:
        row = tk.Frame(frame_form)
        row.pack(pady=5)
        lbl = tk.Label(row, text=label, width=30, anchor='w')
        lbl.pack(side=tk.LEFT)
        entry = tk.Entry(row, width=40)
        entry.pack(side=tk.LEFT)
        entries[label] = entry

    # Combobox para Nível de Acesso
    row_nivel = tk.Frame(frame_form)
    row_nivel.pack(pady=5)
    lbl_nivel = tk.Label(row_nivel, text="Nível de Acesso:", width=30, anchor='w')
    lbl_nivel.pack(side=tk.LEFT)
    nivel_var = tk.StringVar()
    combo_nivel = ttk.Combobox(row_nivel, textvariable=nivel_var, state="readonly", width=38)
    combo_nivel["values"] = ["1 - Administrador", "2 - Funcionario", "3 - Gerente"]
    combo_nivel.current(0)
    combo_nivel.pack(side=tk.LEFT)

    # Função para Salvar Usuário
    def salvar_usuario():
        try:
            nome = entries["Nome"].get()
            usuario = entries["Usuário"].get()
            senha = entries["Senha"].get()
            nivel_selecionado = nivel_var.get().split(" - ")[0]

            if criar_usuario(nome, usuario, senha, int(nivel_selecionado)):
                status_msg.config(text="Usuário cadastrado com sucesso!", fg="green")
                for entry in entries.values():
                    entry.delete(0, tk.END)
                combo_nivel.current(0)
                atualizar_tabela()
        except Exception as e:
            status_msg.config(text=f"Erro ao cadastrar usuário: {e}", fg="red")

    btn_salvar = tk.Button(content_frame, text="Salvar Usuário", command=salvar_usuario)
    btn_salvar.pack(pady=10)

    # Tabela de Usuários
    frame_lista = tk.Frame(content_frame)
    frame_lista.pack(pady=20)

    colunas = ["ID", "Nome", "Usuário", "Nível"]
    tree = ttk.Treeview(frame_lista, columns=colunas, show="headings", height=10)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(side=tk.LEFT)

    # Função para Atualizar a Tabela
    def atualizar_tabela():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, usuario, nivel FROM funcionarios")
        resultados = cursor.fetchall()
        conn.close()

        for item in tree.get_children():
            tree.delete(item)

        for row in resultados:
            if row[3] == 1:
                nivel_label = "Administrador"
            elif row[3] == 2:
                nivel_label = "Comum"
            elif row[3] == 3:
                nivel_label = "Gerente"
            tree.insert("", tk.END, values=(row[0], row[1], row[2], nivel_label))

    atualizar_tabela()

    # Botão para Atualizar a Página
    btn_atualizar = tk.Button(content_frame, text="Atualizar Página", command=atualizar_tabela)
    btn_atualizar.pack(pady=10)

    # Funções para Alterar e Excluir Usuários
    def alterar_usuario():
        item = tree.selection()
        if not item:
            messagebox.showerror("Erro", "Selecione um usuário para alterar.")
            return

        id_usuario = tree.item(item, "values")[0]
        novo_nivel = 1 if messagebox.askyesno("Alterar Nível", "Tornar Administrador?") else 2

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE funcionarios SET nivel = ? WHERE id = ?", (novo_nivel, id_usuario))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Nível de acesso atualizado com sucesso!")
        atualizar_tabela()

    def excluir_usuario():
        item = tree.selection()
        if not item:
            messagebox.showerror("Erro", "Selecione um usuário para excluir.")
            return

        id_usuario = tree.item(item, "values")[0]

        if not messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir este usuário?"):
            return

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_usuario,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
        atualizar_tabela()

    # Botões para Alterar e Excluir
    btn_alterar = tk.Button(content_frame, text="Alterar Nível", command=alterar_usuario)
    btn_alterar.pack(pady=5)

    btn_excluir = tk.Button(content_frame, text="Excluir Usuário", command=excluir_usuario)
    btn_excluir.pack(pady=5)
