def encontrar_palindromos(lista_strings):
    return [s for s in lista_strings if s == s[::-1]]

# Exemplo de uso
lista_strings = ["arara", "python", "radar", "nuvem", "ana", "civic", "palavra"]
lista_palindromos = encontrar_palindromos(lista_strings)

print("Lista original de strings:", lista_strings)
print("Lista de strings palíndromos:", lista_palindromos)
