galera = list()
dado = list()
maior = menor = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa, idade in galera:
    print(f'{pessoa}', end=' ')
    if idade >= 21:
        print(f'é maior de idade')
        maior += 1
    else:
        print(f' é menor de idade')
        menor += 1
print(f'Temos o total de {maior} maiores de idade ')
print(f'Temos o total de {menor} menores de idades')