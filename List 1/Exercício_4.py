pedido_num1 = float (input('Digite um número: '))

pedido_num2 = float (input('Digite outro número: '))

pedido3 = input ('Você deseja somar, subtrair, multiplicar ou dividir?\n(Digite uma dessas opções: +, -, *, /.)\n:')

if pedido3 == ('+'):
    print(f'A soma de {pedido_num1} com {pedido_num2} é: {pedido_num1+pedido_num2}.')

elif pedido3 == ('-'):
    print(f'A subtração de {pedido_num1} com {pedido_num2} é: {pedido_num1-pedido_num2}')

elif pedido3 == ('*'):
    print(f'A multiplicação de {pedido_num1} com {pedido_num2} é: {pedido_num1*pedido_num2}')

elif pedido3 == ('/'):
    print(f'A divisão de {pedido_num1} com {pedido_num2} é: {pedido_num1/pedido_num2}')