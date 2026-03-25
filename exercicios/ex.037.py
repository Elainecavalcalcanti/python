import math
Digite_num=int(input('Digite um númeor inteiro: '))
print(""" Escolha uma das bases parar conversao:
      [ 1 ]  converter para BINÁRIO
      [ 2 ]  converter para OCTAL
      [ 3 ]  converter para HEXADECIMAL""")
Opcao=int(input('Sua opcao:'))

if Opcao== 1:
    binario = bin(Digite_num)
    print(f'{Digite_num} Convertido para BINÁRIO é iagual a {binario}')

elif Opcao == 2:
    octal = oct(Digite_num)
    print(f'{Digite_num} Convertido para BINÁRIO é iagual a {octal}')

elif Opcao == 3:
    hexa = hex(Digite_num)
    print(f'{Digite_num} Convertiddo para HEXADECIMAL é igual a {hexa}')


else:
    print('Opcao nao valida! Digite novamente.')
