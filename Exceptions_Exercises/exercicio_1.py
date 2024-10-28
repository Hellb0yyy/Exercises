try:
    num_1= int(input('Insira um numero:'))
    num_2 = int(input('Insira outro numero:'))
    div = num_1/num_2

    print(f'A divisão de {num_1} com {num_2} é: {div}')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero, insira um número válido.')
except ValueError:
    print('Insira apenas números.')