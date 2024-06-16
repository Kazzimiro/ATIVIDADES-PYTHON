def cores_maiores_que_quatro_letras(cores):
    return {cor for cor in cores if len(cor) > 4}

# Exemplo de uso
conjunto_cores = {"vermelho", "azul", "verde", "amarelo", "preto", "branco", "rosa", "cinza"}
cores_filtradas = cores_maiores_que_quatro_letras(conjunto_cores)

print("Conjunto original de cores:", conjunto_cores)
print("Cores com mais de quatro letras:", cores_filtradas)
