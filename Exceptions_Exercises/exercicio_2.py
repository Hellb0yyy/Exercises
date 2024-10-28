cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul':(0, 0, 255)}

try: 
 cor = input('Insira o nome de uma cor (vermelho, verde ou azul): ')

 rgb = cores[cor]
 print(f'O valor RGB da cor {cor} é: {rgb}')

except KeyError:
 print(f'Cor não encontrada. Tente novamente.')