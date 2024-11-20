import sqlite3

def initialize_db():
    # Conecta ao banco de dados
    conn = sqlite3.connect('components_store.db')
    cursor = conn.cursor()

    # Criação da tabela de componentes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS componentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo TEXT UNIQUE,
            fabricante TEXT,
            categoria TEXT,
            subcategoria TEXT,
            especificacoes TEXT,
            fornecedor TEXT,
            preco_custo REAL,
            preco_venda REAL,
            quantidade INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Inicializar o banco de dados
if __name__ == "__main__":
    initialize_db()

#def alterar_estrutura_tabela():
#    conn = sqlite3.connect('components_store.db')
#    cursor = conn.cursor()
#    try:
#        # Adiciona a coluna quantidade se não existir
#        cursor.execute("ALTER TABLE componentes ADD COLUMN quantidade INTEGER DEFAULT 0")
#        conn.commit()
#        print("Coluna 'quantidade' adicionada com sucesso!")
#    except sqlite3.OperationalError:
#        print("Coluna 'quantidade' já existe.")
#    conn.close()
#
#if __name__ == "__main__":
#    alterar_estrutura_tabela()