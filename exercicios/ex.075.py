
valores = (int(input('Digite um número: ')),
        int(input('Digite outro um numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o último numero: ')))

print(f'Voce digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}º posicao')
else:
    print('Nao foi encontrado 3 nos valores')
print(f'Os valores pares digitados foram', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
