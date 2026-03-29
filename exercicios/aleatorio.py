from random import randint

def sorteio(valores):
    for cont in range(0,10):
        valor = randint(1,50)
        valores.append(valor)
    print(f'Valores sorteados:', end=' ')
    for v in valores:
        print(f'{v}', end=' ')

def analise(valores):
    contapar = contimpar = 0
    for v in valores:
        if v % 2 == 0:
            contapar += 1
        else:
            contimpar += 1
    print()
    print(f'temos {contapar} valores pares')
    print(f'Temos {contimpar} valores impares')

valores = []
sorteio(valores)
analise(valores)
