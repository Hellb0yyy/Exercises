def transferencia_bancaria(saldo, valor_transferencia):
    if valor_transferencia > saldo:
        raise ValueError('Saldo insuficiente.')
    
    saldo -= valor_transferencia
    return saldo

try: 
    saldo = float(input('Digite o saldo da conta: '))
    valor_transferencia = float(input('Digite o valor da tranferência: '))
    saldo_restante = transferencia_bancaria(saldo,valor_transferencia)
    print(f'A transferência foi realizada com sucesso!\nSaldo restante: R${saldo_restante:.2f}')

except ValueError as e:
    print(f'Erro:{e}')
except Exception:
    print('Ocorreu um erro inesperado. Tente novamente.')
finally:
    print('Encerrando Sistema..')