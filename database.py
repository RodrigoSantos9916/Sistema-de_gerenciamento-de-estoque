import sqlite3

conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Produtos (
    ID INTEGER PRIMARY KEY,
    Nome TEXT,
    Descricao TEXT,
    Quantidade INTEGER,
    Preco REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Vendas (
    ID INTEGER PRIMARY KEY,
    ProdutoID INTEGER,
    Quantidade INTEGER,
    Data TEXT,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ID)
)
''')

conn.commit()
conn.close()