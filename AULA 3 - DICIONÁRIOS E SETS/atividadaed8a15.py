------------------------------------------------------------------------------------# Atividade 8
def exibir_informacoes_pessoas(pessoas):
    for nome, idade in pessoas.items():
        print(f"Nome: {nome}, Idade: {idade}")

def main():
    pessoas = {
        "Alice": 30,
        "Bob": 25,
        "Carlos": 40,
        "Diana": 35
    }
    
    print("Informações das pessoas:")
    exibir_informacoes_pessoas(pessoas)

if __name__ == "__main__":
    main()


------------------------------------------------------------------------------------# Atividade 9
def exibir_chaves(dicionario):
    print("Chaves do dicionário:")
    for chave in dicionario.keys():
        print(chave)

def exibir_valores(dicionario):
    print("\nValores do dicionário:")
    for valor in dicionario.values():
        print(valor)

def main():
    pessoas = {
        "Alice": 30,
        "Artur": 25,
        "Henrique": 40,
        "Luan": 35
    }
    
    exibir_chaves(pessoas)
    exibir_valores(pessoas)

if __name__ == "__main__":

------------------------------------------------------------------------------------  # Atividade 10

  def adicionar_ou_atualizar(dicionario, chave, valor):
    dicionario[chave] = valor

def main():
    pessoas = {
        "Alice": 30,
        "Artur": 25,
        "Henrique": 40
    }
    
    chave = input("Digite a chave: ")
    valor = int(input("Digite o valor: "))
    
    adicionar_ou_atualizar(pessoas, chave, valor)
    
    print(pessoas)

if __name__ == "__main__":
    main()

------------------------------------------------------------------------------------  # Atividade 11

def verificar_chaves(dicionario, lista_chaves):
    for chave in lista_chaves:
        if chave not in dicionario:
            return False
    return True

def main():
    pessoas = {
        "Alice": 30,
        "Artur": 25,
        "Henrique": 40,
        "Luan": 35
    }
    
    lista_chaves = ["Alice", "Artur", "Henrique"]
    
    resultado = verificar_chaves(pessoas, lista_chaves)
    print(resultado)

if __name__ == "__main__":
    main()

------------------------------------------------------------------------------------  # Atividade 12

def exibir_menu():
    print("\nOpções de Votação:")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")
    print("0. Encerrar e exibir resultados")

def main():
    votos = {
        "Candidato A": 0,
        "Candidato B": 0,
        "Candidato C": 0
    }
    
    while True:
        exibir_menu()
        escolha = input("Digite sua escolha: ")
        
        if escolha == '0':
            break
        elif escolha == '1':
            votos["Candidato A"] += 1
        elif escolha == '2':
            votos["Candidato B"] += 1
        elif escolha == '3':
            votos["Candidato C"] += 1
        else:
            print("Opção inválida. Por favor, tente novamente.")
    
    print("\nResultados Finais:")
    for candidato, total_votos in votos.items():
        print(f"{candidato}: {total_votos} votos")

if __name__ == "__main__":
    main()
  
------------------------------------------------------------------------------------  # Atividade 13
    notas_alunos = {
        "Alice": 8.5,
        "Bob": 7.2,
        "Carlos": 9.0,
        "Diana": 6.8,
        "Eva": 7.5
    }

    media_notas = sum(notas_alunos.values()) / len(notas_alunos)
    print(f"Média das notas dos alunos: {media_notas:.2f}")

------------------------------------------------------------------------------------  # Atividade 14

    numeros = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 9, 4, 5]
    
    lista_original = numeros[:]
    lista_sem_duplicatas = list(set(numeros))
    
    print(f"Lista original: {lista_original}")
    print(f"Lista sem duplicatas: {lista_sem_duplicatas}")

------------------------------------------------------------------------------------  # Atividade 15

    conjunto1 = {1, 2, 3}
    conjunto2 = {2, 3, 4}
    conjunto3 = {3, 4, 5}

    conjunto_uniao = conjunto1.union(conjunto2, conjunto3)

    print(f"Conjunto união: {conjunto_uniao}")

