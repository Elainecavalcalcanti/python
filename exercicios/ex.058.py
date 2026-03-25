from random import randint

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

computador = randint(0, 10) # O computador pensa no número aqui
tentativas = 0
acertou = False

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print(f'Acertou com {tentativas} tentativas. Parabéns!')