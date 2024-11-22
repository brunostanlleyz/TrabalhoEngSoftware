import tkinter as tk
from cadastro_componentes import cadastro_componentes
from controle_estoque import controle_estoque
from consulta_estoque import consulta_estoque
from database import initialize_db
from cadastro_fornecedores import cadastro_fornecedores
from login import SistemaLogin
from utils import criar_usuario

# Classe principal do sistema
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controle de Estoque - Loja de Eletrônicos")
        self.geometry("900x600")
        self.configure(bg="#f0f0f0")

        # Inicializar o banco de dados
        initialize_db()

        # Frame de navegação e conteúdo
        self.menu_frame = tk.Frame(self, bg="#ffffff")
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.content_frame = tk.Frame(self, bg="#e0e0e0")
        self.content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Botões do Menu
        self.create_menu_buttons()

    def create_menu_buttons(self):
        btn_cadastro = tk.Button(self.menu_frame, text="Cadastro de Componentes", width=25, 
                                 command=lambda: cadastro_componentes(self.content_frame))
        btn_cadastro.pack(pady=5)

        btn_estoque = tk.Button(self.menu_frame, text="Controle de Estoque", width=25, 
                                command=lambda: controle_estoque(self.content_frame))
        btn_estoque.pack(pady=5)

        btn_consulta = tk.Button(self.menu_frame, text="Consulta de Estoque", width=25,
                                 command=lambda: consulta_estoque(self.content_frame))
        btn_consulta.pack(pady=5)

        btn_fornecedores = tk.Button(self.menu_frame, text="Cadastro de Fornecedores", width=25,
                                     command=lambda: cadastro_fornecedores(self.content_frame))
        btn_fornecedores.pack(pady=5)

if __name__ == "__main__":
    #app = App()
    #app.mainloop()
    initialize_db()

    #Executar só uma vez para criar o usuário e testar o sistema de login
    #criar_usuario('Administrador', 'admin', '1234', 'admin')

    root = tk.Tk()
    app = SistemaLogin(root)
    root.mainloop()