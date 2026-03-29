from random import randint
def sorteio(numeros):
    for cont in range(0,5):
        numeros.append(randint(1,10))
    print(f'Sorteando 5 valor da lista: ',end=' ')
    for n in numeros:
        print(f'{n}',end=' ')
    print('PRONTO')

def par(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores de {numeros}, temos {soma}')

numeros = list()
sorteio(numeros)
par(numeros)
