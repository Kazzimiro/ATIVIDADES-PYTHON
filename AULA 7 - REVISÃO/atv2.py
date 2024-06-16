def filtrar_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]

# Exemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = filtrar_pares(lista_numeros)

print("Lista original:", lista_numeros)
print("Lista de números pares:", lista_pares)
