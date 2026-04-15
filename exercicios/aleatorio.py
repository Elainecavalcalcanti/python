def idadeMaior(msg):
    ok = False
    valor = 0
    while True:
        i = input(msg)
        if i.isnumeric():
            valor = int(int)
            if 0 <= i <= 200:
                ok = True
            else:
                print('Idade invalida, tente novamente.')
        if ok:
            break
    return valor

i = idadeMaior('Digite sua idade: ')
print(f'Você tem {i} anos.')