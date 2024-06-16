def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_notas = calcular_media(nota1, nota2, nota3)

print(f"A média das notas {nota1}, {nota2} e {nota3} é: {media_notas:.2f}")
