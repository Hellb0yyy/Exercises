lista_clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    lista_clientes.append(cliente)
    print(f'O cliente {nome} foi adicionado com êxito.')


def exibir_clientes():
    if not lista_clientes:
     print('Nenhum cliente encontrado.')

    else:
       for i, cliente in enumerate(lista_clientes, start=1):
          print (f'Cliente {i}:')
          print (f'Nome: {cliente[0]}')
          print (f'Email: {cliente[1]}')
          print (f'Telefone: {cliente[2]}')
          print (f'Endereço: {cliente[3]}')

def buscar_cliente(email):
 for cliente in lista_clientes:
    if cliente[1] == email:
     print('Cliente encontrado:')
     print (f'Nome: {cliente[0]}')
     print (f'Email: {cliente[1]}')
     print (f'Telefone: {cliente[2]}')
     print (f'Endereço: {cliente[3]}')
     return cliente
 print ('Cliente não encontrado.')
 return None
      
def remover_cliente(email):
   cliente = buscar_cliente(email)
   if cliente:
      lista_clientes.remove(cliente)
      print(f'O cliente com o email {email} foi removido com êxito.')
   else: 
      print(f'Não foi possível remover o cliente com o email {email}.')      


def menu():
   while True:
      print('Sistema de Cadastro de Clientes')
      print('1. Adicionar Cliente')
      print('2. Exibir Clientes')
      print('3. Buscar Clientes')
      print('4. Remover Cliente')
      print('5. Sair')

      escolha = input('Escolha uma opção:')

      if escolha == '1':
         nome = input('Digite o nome do cliente:')
         email = input('Digite o email do cliente:')
         telefone = input('Digite o telefone do cliente:')
         endereco = input('Digite o endereço do cliente:')
         adicionar_cliente(nome, email, telefone, endereco)
      
      elif escolha == '2':
         exibir_clientes()

      elif escolha == '3':
         email = input('Digite o email do cliente para ser encontrado:')
         buscar_cliente(email)

      elif escolha == '4':
         email = input('Digite o email do cliente para ser removido:')
         remover_cliente(email)

      elif escolha == '5':
         print('Fechando sistema...')
         break

menu()
