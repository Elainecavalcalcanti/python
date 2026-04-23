def leiaNota(msg):
    ok =False
    nota = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            nota = int(n)
            if 0 <= n <= 10:
                ok = True
            else:
                print('Nota invalida. Tente novamente!')
        if ok:
            break
        return nota
n = leiaNota('Digite sua nota: ')
print(f'Sua nota foi {n}')