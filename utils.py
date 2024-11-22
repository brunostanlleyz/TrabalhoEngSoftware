import sqlite3
from tkinter import messagebox

# Função para salvar o componente no banco de dados
def save_component(data):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = '''
        INSERT INTO componentes (nome, codigo, fabricante, categoria, subcategoria, especificacoes, fornecedor, preco_custo, preco_venda)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(query, data)
        conn.commit()
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar componente: {e}")
        return False
    finally:
        conn.close()

# Função para salvar o fornecedor no banco de dados
def save_supplier(data):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = '''
        INSERT INTO fornecedores (nome, cnpj, email, telefone, endereco)
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(query, data)
        conn.commit()
        return True
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar fornecedor: {e}")
        return False
    finally:
        conn.close()


def criar_usuario(nome, usuario, senha, nivel):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO funcionarios (nome, usuario, senha, nivel)
            VALUES (?, ?, ?, ?)
        """, (nome, usuario, senha, nivel))
        conn.commit()
        print(f"Usuário '{usuario}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        conn.close()