try:
 
 num = int(input('Insira um número:'))

 if num > 10 :
  print('O número é valido')
 
except ValueError:

 print("Por favor, insira um número válido.")
else:

 print('O programa foi executado com sucesso.')
finally:
  print('Programa encerrado.')