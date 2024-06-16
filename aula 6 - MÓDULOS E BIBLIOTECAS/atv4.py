import random

def jogo_adivinhacao():
    numero_para_adivinhar = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_para_adivinhar:
            print("Tente um número maior...")
        elif palpite > numero_para_adivinhar:
            print("Tente um número menor...")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
if __name__ == "__main__":
    jogo_adivinhacao()
