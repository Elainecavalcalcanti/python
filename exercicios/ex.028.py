import random
print('-='*20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-='*20)
jogador =int(input('Em que número e pensei? '))
computador = random.randint(0,5)

if jogador == computador :
    print(f'PARABÉNS! Voce conseguiu vencer! seu numero foi {jogador} e sorteado {computador}')
else:
    print(f'GANHEI! Eu pensei no numero {computador} nao no {jogador} ')
