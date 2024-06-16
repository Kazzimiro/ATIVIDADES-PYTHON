#------------------MÓDULO MANIPULAÇÃO ----------------#

def inverter_string(texto):
    return texto[::-1]

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


#----------------- PROGRAMA PRINCIPAL ----------------#

import manipulacao_strings

def exibir_menu():
    print("### Operações com Strings ###")
    print("1 - Inverter uma string")
    print("2 - Contar o número de palavras em uma string")
    print("3 - Verificar se uma string é um palíndromo")
    print("4 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            texto = input("Digite a string que deseja inverter: ")
            resultado = manipulacao_strings.inverter_string(texto)
            print(f"String invertida: {resultado}")
        elif opcao == '2':
            texto = input("Digite a string que deseja contar as palavras: ")
            resultado = manipulacao_strings.contar_palavras(texto)
            print(f"Número de palavras: {resultado}")
        elif opcao == '3':
            texto = input("Digite a string que deseja verificar se é um palíndromo: ")
            if manipulacao_strings.eh_palindromo(texto):
                print("A string é um palíndromo!")
            else:
                print("A string não é um palíndromo.")
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")

if __name__ == "__main__":
    main()
