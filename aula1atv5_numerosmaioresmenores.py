numeros = []

for i in range(5):
        numero = float(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)

menor = numeros[0]
maior = numeros[0]
soma = 0

for numero in numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
        soma += numero

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
