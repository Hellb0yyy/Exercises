pedido_vogais = input('Digite alguma palavra para ver as vogais dela: ')

vogais = ('aeiouAEIOU')

contador = 0

for carac in pedido_vogais:
    if carac in vogais:
        contador += 1

print(f"O número de vogais na string é: {contador}")
