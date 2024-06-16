def encontrar_produto_mais_vendido(vendas):
    max_vendas = max(vendas.values())
    produtos_mais_vendidos = [produto for produto, quantidade in vendas.items() if quantidade == max_vendas]
    return produtos_mais_vendidos

# Exemplo de uso
vendas_produtos = {
    "produto_a": 150,
    "produto_b": 200,
    "produto_c": 200,
    "produto_d": 180,
    "produto_e": 50
}

produtos_mais_vendidos = encontrar_produto_mais_vendido(vendas_produtos)

print("Dicionário de vendas:", vendas_produtos)
print("Produto(s) mais vendido(s):", produtos_mais_vendidos)
