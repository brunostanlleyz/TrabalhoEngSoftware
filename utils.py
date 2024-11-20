import sqlite3
from tkinter import messagebox

# Função para salvar o componente no banco de dados
def save_component(data):
    try:
        conn = sqlite3.connect('components_store.db')
        cursor = conn.cursor()

        query = '''
        INSERT INTO componentes (nome, codigo, fabricante, categoria, subcategoria, especificacoes, fornecedor, preco_custo, preco_venda)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar componente: {e}")
        return False

# Função para salvar o fornecedor no banco de dados
def save_supplier(data):
    try:
        conn = sqlite3.connect('components_store.db')
        cursor = conn.cursor()

        query = '''
        INSERT INTO fornecedores (nome, cnpj, email, telefone, endereco)
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar fornecedor: {e}")
        return False