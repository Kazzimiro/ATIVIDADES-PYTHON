--------------------------------# Módulo de Operacoes-----------------------

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida"


--------------------------------# Arquivo prinicipal--------------------------

import operacoes

def exibir_menu():
    print("### Calculadora ###")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = operacoes.soma(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = operacoes.subtracao(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = operacoes.multiplicacao(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == '4':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = operacoes.divisao(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 5.")

if __name__ == "__main__":
    main()
