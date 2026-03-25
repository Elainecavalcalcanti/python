cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=' ') 
    resp = str(input('Voce quer continuar? [S/N] ')).upper().strip()[0]       
print(f'Voce digitou o numero {cont[num]}')