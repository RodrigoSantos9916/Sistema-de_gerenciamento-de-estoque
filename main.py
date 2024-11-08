from classes import Produto, Venda, GerenciadorDeEstoque

gerenciador = GerenciadorDeEstoque('estoque.db')

produto1 = Produto(1, 'Notebook', 'Notebook Dell', 10, 3500.00)
produto2 = Produto(2, 'Mouse', 'Mouse Logitech', 50, 150.00)
gerenciador.adicionar_produto(produto1)
gerenciador.adicionar_produto(produto2)

gerenciador.atualizar_quantidade(1, 8)

venda1 = Venda(1, 1, 2, '2024-10-19')
gerenciador.registrar_venda(venda1)

relatorio = gerenciador.gerar_relatorio_estoque()
for linha in relatorio:
    print(linha)

gerenciador.fechar_conexao()