def verificar_senha(senha):
    if len(senha) < 8:
        raise ValueError('A senha deve ter no mínimo 8 caracteres.')
    
    if not any(crt.isdigit() for crt in senha):
        raise ValueError('A senha deve ter pelo menos um número.')
    
    return 'Senha válida.'

try:
    senha_usuario = input('Digite a senha:')
    resultado = verificar_senha(senha_usuario)

    print (resultado)

except ValueError as e:
    print(f'Erro: {e}')

finally:
    print('Programa encerrado.')