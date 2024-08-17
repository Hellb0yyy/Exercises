pedido_list_num = input("Digite uma lista de números separados por espaço: ")

numeros = [float(num) for num in pedido_list_num.split()]

maior_num = max(numeros)

print(f'O maior número da lista é: {maior_num}')