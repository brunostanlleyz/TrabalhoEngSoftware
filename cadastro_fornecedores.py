import tkinter as tk
from tkinter import messagebox
from utils import save_component, save_supplier

# Função para criar a interface de cadastro de fornecedores
def cadastro_fornecedores(content_frame):
    # Limpa a tela atual
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    title = tk.Label(content_frame, text="Cadastro de Fornecedores", font=("Arial", 14))
    title.pack(pady=10)

    labels = ["Nome", "CNPJ", "Endereço", "Telefone", "Email"]

    entries = {}
    for label in labels:
        frame = tk.Frame(content_frame)
        frame.pack(pady=5)
        lbl = tk.Label(frame, text=label, width=20, anchor='w')
        lbl.pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=40)
        entry.pack(side=tk.LEFT)
        entries[label] = entry

    # Função para submeter os dados do formulário
    def submit():
        data = tuple(entry.get() for entry in entries.values())

        if save_supplier(data):
            messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")
            for entry in entries.values():
                entry.delete(0, tk.END)

    submit_button = tk.Button(content_frame, text="Salvar Fornecedor", command=submit)
    submit_button.pack(pady=10)