totmaior = totman = mulher = 0 
while True:
    print('-'*25)
    print('CADRASTRO DE PESSOAS')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
    print('-'*25)
    if idade >= 18:
        totmaior += 1
    if sexo =='M':
        totman += 1
    if idade <20 and sexo == 'F':
        mulher += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if c == 'N':
        break
print(f'{totmaior} pessoas tem mais de 18 anos.')
print(f'{totman} homens foram cadastrados.')
print(f'{mulher} mulheres foram cadastradas e tem menos de 20 anos.')