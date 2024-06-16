# COMO TEREMOS QWUE USAR VARIOS MÓDULOS, TEREMOS QQUE UTILIZAR DE CÓDIGOS DEDICADOS PARA CADA ATIVIDADE SUGERIDA #

------------------------------------------- # conversao_comprimento.py ---------------------------------------------

def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes / 3.28084

------------------------------------------- # conversao_peso.py ---------------------------------------------

def quilogramas_para_libras(quilogramas):
    return quilogramas * 2.20462

def libras_para_quilogramas(libras):
    return libras / 2.20462

------------------------------------------- # conversao_temperatura.py ---------------------------------------------

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


------------------------------------------- # PROGRAMA PRINCIPAL --------------------------------------------------
import conversao_comprimento
import conversao_peso
import conversao_temperatura

def menu():
    print("Escolha o tipo de conversão:")
    print("1. Comprimento (metros <-> pés)")
    print("2. Peso (quilogramas <-> libras)")
    print("3. Temperatura (Celsius <-> Fahrenheit)")
    print("0. Sair")
    return input("Digite a opção desejada: ")

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            print("1. Metros para Pés")
            print("2. Pés para Metros")
            escolha = input("Digite a opção desejada: ")
            valor = float(input("Digite o valor a ser convertido: "))
            if escolha == '1':
                resultado = conversao_comprimento.metros_para_pes(valor)
                print(f"{valor} metros = {resultado} pés")
            elif escolha == '2':
                resultado = conversao_comprimento.pes_para_metros(valor)
                print(f"{valor} pés = {resultado} metros")

        elif opcao == '2':
            print("1. Quilogramas para Libras")
            print("2. Libras para Quilogramas")
            escolha = input("Digite a opção desejada: ")
            valor = float(input("Digite o valor a ser convertido: "))
            if escolha == '1':
                resultado = conversao_peso.quilogramas_para_libras(valor)
                print(f"{valor} quilogramas = {resultado} libras")
            elif escolha == '2':
                resultado = conversao_peso.libras_para_quilogramas(valor)
                print(f"{valor} libras = {resultado} quilogramas")

        elif opcao == '3':
            print("1. Celsius para Fahrenheit")
            print("2. Fahrenheit para Celsius")
            escolha = input("Digite a opção desejada: ")
            valor = float(input("Digite o valor a ser convertido: "))
            if escolha == '1':
                resultado = conversao_temperatura.celsius_para_fahrenheit(valor)
                print(f"{valor} Celsius = {resultado} Fahrenheit")
            elif escolha == '2':
                resultado = conversao_temperatura.fahrenheit_para_celsius(valor)
                print(f"{valor} Fahrenheit = {resultado} Celsius")

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
