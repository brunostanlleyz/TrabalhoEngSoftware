import sqlite3

def initialize_db():
    # Conecta ao banco de dados
    conn = sqlite3.connect('components_store.db')
    cursor = conn.cursor()

    # Criação da tabela de fornecedores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fornecedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT UNIQUE,
            email TEXT,
            telefone TEXT,
            endereco TEXT
        )
    ''')

    conn.commit()
    conn.close()