
def saudacao_por_horario(hora):
    if 6 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")

# Exemplo de uso da função:
hora_atual = int(input("Digite a hora (0-23): "))
saudacao_por_horario(hora_atual)

