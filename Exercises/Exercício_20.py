import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Tente adivinhar o número entre 1 e 100!")

    while not acertou:
        tentativa = int(input("Digite seu palpite: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("O número secreto é maior!")
        elif tentativa > numero_secreto:
            print("O número secreto é menor!")
        else:
            acertou = True
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")

adivinhar_numero()
