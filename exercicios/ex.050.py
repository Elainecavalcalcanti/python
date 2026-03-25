
soma = 0
cont = 0
for n in range(0,6):
    n=int(input('Digite um numero inteiro:'))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'Voce informou {cont} números e a soma foi {soma}')
    