lista = {}
total = []
soma = media = 0
while True:

    lista['Nome'] = str(input('Nome: '))
    while True:
        lista['Sexo'] = str(input('Sexo [F/M] ')).upper().strip()[0]
        if lista['Sexo'] in 'FM':
            break
        print('ERRO! Por favor, escolher apenas M ou F.')

    lista['Nota'] = float(input('Nota: '))
    soma += lista['Nota']

    total.append(lista.copy())

    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, escolher apenas S ou N.')
    if resp == 'N':
        break

print(total)
print(f'Ao todo {len(total)} alunos foram cadastrados')
media = soma / len(total)
print(f'A Média das notas dos alunos foram {media:.2f}')
print('Os alunos do sexo Masxculino são: ', end=' ')
for p in total:
    if p['Sexo'] == 'M':
        print(f'{p["Nome"]}', end=' ')

for p in total:
    if p['Nota'] >= 7:
        for k, v in lista.items():
            print(f'{k} = {v}', end=' ')
