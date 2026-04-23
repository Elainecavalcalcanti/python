def idadeMaior(msg):        #funcao
    ok = False              # variavel de controle
    valor = 0               # variavel de aramazenamento de valor
    while True:
        i = input(msg)
        if i.isnumeric():
            valor = int(i)
            if 0 <= valor <= 200:
                ok = True
            else:
                print('Idade invalida, tente novamente.')
        if ok:
            break
    return valor

i = idadeMaior('Digite sua idade: ')
print(f'Você tem {i} anos.')