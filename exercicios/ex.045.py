from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opcoes
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')

print('-='*11)
print(f'O computador jogou {itens[computador]}')
print(f'O Jogador jogou {itens[jogador]}')
print('-='*11)

if computador == 0:    #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
elif computador == 1:      #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
elif computador == 2:         #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 0:
        print('EMPATE')
else:
    print('OPCAO INVALIDA! TENTE NOVAMENTE.')
