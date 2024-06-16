from functools import reduce

def encontrar_maior_string(lista):
    return reduce(lambda x, y: x if len(x) > len(y) else y, lista)

# Exemplo de uso da função:
strings = ["python", "java", "javascript", "ruby", "NodeJs"]
maior_string = encontrar_maior_string(strings)
print(f"A maior string na lista é: {maior_string}")
