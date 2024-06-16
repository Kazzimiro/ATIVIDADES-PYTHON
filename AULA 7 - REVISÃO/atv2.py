#---------------------------------- MODULO DE GERENCIAMENTO ---------------------------------#

def adicionar_produto(produtos, nome, preco, quantidade):
    produtos[nome] = {'preco': preco, 'quantidade': quantidade}

def remover_produto(produtos, nome):
    if nome in produtos:
        del produtos[nome]
    else:
        print(f"O produto {nome} não está no inventário.")

def atualizar_produto(produtos, nome, preco=None, quantidade=None):
    if nome in produtos:
        if preco is not None:
            produtos[nome]['preco'] = preco
        if quantidade is not None:
            produtos[nome]['quantidade'] = quantidade
    else:
        print(f"O produto {nome} não está no inventário.")

  #---------------------------------- PROGRAMA PRINCIPAL ---------------------------------#

import gerenciamento_produtos

def exibir_produtos(produtos):
    for nome, detalhes in produtos.items():
        print(f"Nome: {nome}, Preço: {detalhes['preco']}, Quantidade: {detalhes['quantidade']}")

def menu():
    print("\nMENU PRINCIPAL")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Atualizar Produto")
    print("4. Exibir Produtos")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    produtos = {}
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade em estoque: "))
            gerenciamento_produtos.adicionar_produto(produtos, nome, preco, quantidade)
            print(f"Produto {nome} adicionado com sucesso.")
        
        elif opcao == '2':
            nome = input("Digite o nome do produto a ser removido: ")
            gerenciamento_produtos.remover_produto(produtos, nome)
        
        elif opcao == '3':
            nome = input("Digite o nome do produto a ser atualizado: ")
            preco = input("Digite o novo preço (ou deixe em branco para não alterar): ")
            quantidade = input("Digite a nova quantidade (ou deixe em branco para não alterar): ")
            preco = float(preco) if preco else None
            quantidade = int(quantidade) if quantidade else None
            gerenciamento_produtos.atualizar_produto(produtos, nome, preco, quantidade)
            print(f"Produto {nome} atualizado com sucesso.")
        
        elif opcao == '4':
            exibir_produtos(produtos)
        
        elif opcao == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
