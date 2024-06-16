# Atividade 1
frutas = set()
frutas.update(["maçã", "banana", "uva", "laranja", "morango"])
print("Conjunto de frutas:", frutas)

# Atividade 2
print("A fruta 'banana' está presente no conjunto frutas?", "banana" in frutas)

# Atividade 3
frutas_vermelhas = {"morango", "cereja", "framboesa"}
print("Conjunto de frutas vermelhas:", frutas_vermelhas)

# Atividade 4
frutas_vermelhas.remove("cereja")
print("Conjunto de frutas vermelhas após remover 'cereja':", frutas_vermelhas)

# Atividade 5
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
uniao = A | B
print("União dos conjuntos A e B:", uniao)

# Atividade 6
def intersecao_conjuntos(conj1, conj2):
    return conjunto_1 & conjunto_2

C = {1, 2, 3}
D = {2, 3, 4}
print("Interseção dos conjuntos C e D:", intersecao_conjuntos(C, D))

# Atividade 7
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    return list(conjunto1 | conjunto2)

lista1 = [1, 2, 2, 3, 4]
lista2 = [3, 4, 4, 5, 6]
print("União dos elementos únicos das listas:", uniao_listas(lista1, lista2))
