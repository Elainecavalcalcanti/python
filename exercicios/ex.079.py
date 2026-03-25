numeros = list ()
while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print(f'Número adicionado com sucesso!')
    else:
        print('Numero Duplicado! Não será adicionado.')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')