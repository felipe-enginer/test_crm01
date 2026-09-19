import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "crm.db" #caminho para o b.d

def get_connection():
    """Abre e retorna uma conexão com o banco de dados SQLite."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    """Cria a tabela de clientes no banco caso ela não exista."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            status TEXT NOT NULL,
            valor REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    init_db()
    print("Banco de dados e tabela de clientes criados!")




    