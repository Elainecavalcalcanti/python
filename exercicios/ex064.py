soma = 0
cont = 0
num = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Voce digitou {cont} números e a soma entres ele foi {soma}')
