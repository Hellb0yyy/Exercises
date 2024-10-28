def calcular_media(notas):
    if len(notas) == 0:
        return None
    soma = sum(notas)
    media = soma / len(notas)
    return media

def exibir_media(notas):
    media = calcular_media(notas)
    if media is None:
        print('Não há nenhuma nota inserida, a média não pode ser calculada.')
    else:
        if media > 7:
            print(f'Parabéns!! A sua média é {media:.2f} e você foi aprovado :)')
        else:
            print(f'Sinto muito, a sua média é {media:.2f}. Infelizmente você não foi aprovado :(')

try:
    numero_notas = int(input('Insira o número de notas: '))
    notas = []

    if numero_notas <= 0:
        raise ValueError('O número de notas deve ser maior que zero.')
    
    for i in range(numero_notas):
     while True:
        try:
            nota = float(input(f'Digite a nota {i+1}: '))
            notas.append(nota)
            break
        except ValueError:
            print('Erro: Valor inválido. Insira um número válido.')

    exibir_media(notas)

except ValueError as e:
    print(f'Erro: {e}')
finally:
    print('Programa encerrado.')