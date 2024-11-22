import tkinter as tk
from tkinter import messagebox
from database import connect
import importlib  # Importa o módulo importlib para carregamento dinâmico

class SistemaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")

        # Widgets do Login
        tk.Label(self.root, text="Usuário:").pack(pady=5)
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.pack(pady=5)

        tk.Label(self.root, text="Senha:").pack(pady=5)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.pack(pady=5)

        tk.Button(self.root, text="Entrar", command=self.verificar_login).pack(pady=10)

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        conexao = connect()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM funcionarios WHERE usuario = ? AND senha = ?
        """, (usuario, senha))

        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            self.nivel_acesso = resultado[4]  # Nível do usuário
            messagebox.showinfo("Login Bem-Sucedido", f"Bem-vindo, {usuario}!")
            self.abrir_dashboard()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos!")

    def abrir_dashboard(self):
        # Fecha a tela de login
        self.root.destroy()

        # Usando importlib para importar e rodar o App de forma dinâmica
        app_module = importlib.import_module("main")  # Importa dinamicamente o módulo main
        app = app_module.App(nivel_acesso=self.nivel_acesso)  # Cria uma instância da classe App de main.py
        app.mainloop()  # Roda o loop principal da aplicação
