import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Configuração da Janela Principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controle de Estoque - Loja de Eletrônicos")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")

        # Frame de Navegação
        self.menu_frame = tk.Frame(self, bg="#ffffff")
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Frame de Conteúdo
        self.content_frame = tk.Frame(self, bg="#e0e0e0")
        self.content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Botões do Menu
        self.create_menu_buttons()
        self.create_welcome_screen()

    def create_menu_buttons(self):
        # Botões de navegação
        buttons = [
            ("Cadastro de Componentes", self.show_component_screen),
            ("Cadastro de Fornecedores", self.show_supplier_screen),
            ("Controle de Estoque", self.show_inventory_screen),
            ("Registro de Vendas", self.show_sales_screen),
            ("Relatórios", self.show_reports_screen)
        ]

        for text, command in buttons:
            button = tk.Button(self.menu_frame, text=text, width=20, command=command)
            button.pack(pady=5)

    def create_welcome_screen(self):
        # Tela de boas-vindas
        welcome_label = tk.Label(self.content_frame, text="Bem-vindo ao Sistema de Controle de Estoque", 
                                 font=("Arial", 16), bg="#e0e0e0")
        welcome_label.pack(pady=20)

    def clear_content_frame(self):
        # Limpar o frame de conteúdo
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_component_screen(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Cadastro de Componentes", font=("Arial", 14))
        title.pack(pady=10)

        # Aqui você pode adicionar o formulário de cadastro

    def show_supplier_screen(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Cadastro de Fornecedores", font=("Arial", 14))
        title.pack(pady=10)

        # Aqui você pode adicionar o formulário de cadastro de fornecedores

    def show_inventory_screen(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Controle de Estoque", font=("Arial", 14))
        title.pack(pady=10)

        # Aqui você pode adicionar a interface para controle de estoque

    def show_sales_screen(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Registro de Vendas", font=("Arial", 14))
        title.pack(pady=10)

        # Aqui você pode adicionar o formulário de registro de vendas

    def show_reports_screen(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Relatórios", font=("Arial", 14))
        title.pack(pady=10)

        # Aqui você pode adicionar a interface para visualização de relatórios

if __name__ == "__main__":
    app = App()
    app.mainloop()
