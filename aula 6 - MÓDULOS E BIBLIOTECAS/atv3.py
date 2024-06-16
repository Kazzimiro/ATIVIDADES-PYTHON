import math

def calcular_area_quadrado(lado):
    return lado * lado

def calcular_perimetro_quadrado(lado):
    return 4 * lado

def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

def calcular_perimetro_retangulo(comprimento, largura):
    return 2 * (comprimento + largura)

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

def calcular_perimetro_circulo(raio):
    return 2 * math.pi * raio

def main():
    while True:
        print("\n  Calculadora de Área e Perímetro ")
        print("Escolha a forma geométrica:")
        print("1 - Quadrado")
        print("2 - Retângulo")
        print("3 - Círculo")
        print("4 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            lado = float(input("Digite o lado do quadrado: "))
            area = calcular_area_quadrado(lado)
            perimetro = calcular_perimetro_quadrado(lado)
            print(f"Área do quadrado: {area}")
            print(f"Perímetro do quadrado: {perimetro}")
        elif opcao == '2':
            comprimento = float(input("Digite o comprimento do retângulo: "))
            largura = float(input("Digite a largura do retângulo: "))
            area = calcular_area_retangulo(comprimento, largura)
            perimetro = calcular_perimetro_retangulo(comprimento, largura)
            print(f"Área do retângulo: {area}")
            print(f"Perímetro do retângulo: {perimetro}")
        elif opcao == '3':
            raio = float(input("Digite o raio do círculo: "))
            area = calcular_area_circulo(raio)
            perimetro = calcular_perimetro_circulo(raio)
            print(f"Área do círculo: {area}")
            print(f"Perímetro do círculo: {perimetro}")
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 4.")

if __name__ == "__main__":
    main()
