pessoa = {}
galera  = []

soma = media = 0 
while True:

    pessoa['Nome'] = str(input('Nome: '))

    while True: 
        pessoa['Sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por Favor, digite apenas M ou F.')

    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']

    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por Favor, digite apenas S ou N.')
    if resp == 'N':
        break

print('-='*40)
print(f'A) Ao todo temos {len(galera)} cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadrastradas foram', end=' ')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('D) Lista das Pessoas que estão acima da média')
if p in galera:
    if p['Idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v} ', end=(' '))
        print(' ')

print('<<< ENCERRADO')
        
