import tkinter as tk
from tkinter import messagebox
from utils import save_component

# Função para criar a interface de cadastro de componentes
def cadastro_componentes(content_frame):
    # Limpa a tela atual
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    title = tk.Label(content_frame, text="Cadastro de Componentes", font=("Arial", 14))
    title.pack(pady=10)

    labels = ["Nome", "Código", "Fabricante", "Categoria", "Subcategoria", 
              "Especificações Técnicas", "Fornecedor", "Preço de Custo", "Preço de Venda"]

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
        try:
            preco_custo = float(entries["Preço de Custo"].get())
            preco_venda = float(entries["Preço de Venda"].get())
        except ValueError:
            messagebox.showerror("Erro", "Preço de custo e venda devem ser numéricos")
            return

        data = (
            entries["Nome"].get(),
            entries["Código"].get(),
            entries["Fabricante"].get(),
            entries["Categoria"].get(),
            entries["Subcategoria"].get(),
            entries["Especificações Técnicas"].get(),
            entries["Fornecedor"].get(),
            preco_custo,
            preco_venda
        )

        if save_component(data):
            messagebox.showinfo("Sucesso", "Componente cadastrado com sucesso!")
            for entry in entries.values():
                entry.delete(0, tk.END)

    submit_button = tk.Button(content_frame, text="Salvar Componente", command=submit)
    submit_button.pack(pady=10)
