pedido_numero_primo = int (input('Insira um número para verificar se ele é primo:'))

if pedido_numero_primo > 1:
    for i in range(2, pedido_numero_primo):
        if pedido_numero_primo % i == 0:
            print(f'{pedido_numero_primo} não é primo')
            break
    else:
        print(f'{pedido_numero_primo} é primo')