def calcular_area_retangulo(comprimento, largura):
    area = comprimento * largura
    return area

comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

area_retangulo = calcular_area_retangulo(comprimento, largura)

print(f"A área do retângulo de comprimento {comprimento} e largura {largura} é: {area_retangulo}")
