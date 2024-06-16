def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

# Exemplo de uso da função:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_pares(numeros)
print(resultado)
