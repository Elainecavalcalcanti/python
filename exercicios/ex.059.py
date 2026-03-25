
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
opcao= 0
while opcao != 5:
    print('-='*20)
    print('''      [ 1 ] Somar
      [ 2 ] Multiplicar
      [ 3 ] Maior
      [ 4 ] Novos Números
      [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opcao? '))

    if opcao == 1:
        print(f'O resultado de {n1} + {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif opcao ==3:
        if n1 > n2:
            print(f'O maior valor entre {n1} e {n2} é : {n1} ')
        else:
            print(f'O maior valor entre {n1} e {n2} é : {n2} ')
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro Número:'))
        n2 = int(input('Primeiro Número:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
        print('-='*20)
