while True:
    print('-'*40)
    n = int(input('Quer ver a tabuada de que valor? '))
    if n < 0:
        break
    print('-'*40)
    for c in range (1,11):
        print(f'{n} X {c} = {n*c}')
print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')