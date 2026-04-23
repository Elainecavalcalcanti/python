def ajuda(com):
    help(com)



def titulo(msg, cor):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


comando = ''
while True:
    comando = str(input("Função ou biblioteca> "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!')