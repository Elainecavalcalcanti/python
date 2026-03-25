from random import randint
v = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'* 15)
while True:
    jogador=int(input('Diga um valor: '))
    computador = randint(0,10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Voce VENCEU')
            v+= 1
        else:
            print('Voce PERDEU ')
            break
    elif tipo == 'I':
        if soma  % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU')
            break
print('Vamos joagar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')