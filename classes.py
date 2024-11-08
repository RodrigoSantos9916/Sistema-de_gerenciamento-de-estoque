import sqlite3

class Produto:
    def __init__(self, id, nome, descricao, quantidade, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

class Venda:
    def __init__(self, id, produto_id, quantidade, data):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data = data

class GerenciadorDeEstoque:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def adicionar_produto(self, produto):
        self.cursor.execute('''
        INSERT INTO Produtos (ID, Nome, Descricao, Quantidade, Preco)
        VALUES (?, ?, ?, ?, ?)
        ''', (produto.id, produto.nome, produto.descricao, produto.quantidade, produto.preco))
        self.conn.commit()

    def atualizar_quantidade(self, produto_id, quantidade):
        self.cursor.execute('''
        UPDATE Produtos
        SET Quantidade = ?
        WHERE ID = ?
        ''', (quantidade, produto_id))
        self.conn.commit()

    def registrar_venda(self, venda):
        self.cursor.execute('''
        INSERT INTO Vendas (ID, ProdutoID, Quantidade, Data)
        VALUES (?, ?, ?, ?)
        ''', (venda.id, venda.produto_id, venda.quantidade, venda.data))
        self.conn.commit()
        self.atualizar_quantidade(venda.produto_id, self.obter_quantidade(venda.produto_id) - venda.quantidade)

    def obter_quantidade(self, produto_id):
        self.cursor.execute('''
        SELECT Quantidade FROM Produtos WHERE ID = ?
        ''', (produto_id,))
        return self.cursor.fetchone()[0]

    def gerar_relatorio_estoque(self):
        self.cursor.execute('''
        SELECT * FROM Produtos
        ''')
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()