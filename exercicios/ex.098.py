from time import sleep
def contador(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if p < 0:
        p*=- 1
    if p == 0:
        p = 1 

    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep(0.5)
        print('FIM')
    else: 
        cont = i 
        while cont >= f:
            print(f'{cont}', end=' ',flush=True)
            cont -= p
            sleep(0.5)
            print('FIM')

contador(1,10,1)
print('-='*20)
print('Agora é a sua vez de personalizar.')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini,fim,pas)