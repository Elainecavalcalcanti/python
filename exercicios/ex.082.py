lista = []
pares = []
impar = []
while True:
    n =(int(input('Digite um numero: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impar.append(n)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de números pares é:{pares}')
print(f'A lista de números impares é:{impar}')
