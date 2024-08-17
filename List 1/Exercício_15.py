num_input= input('Digite uma lista de números separados por espaço: ')

num = [int(numero) for numero in num_input.split()]

num_par = [numero for numero in num if numero % 2 == 0 ]

print(f'Os números pares da lista são: {num_par}')