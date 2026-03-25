sal = float(input('Qual é o salário do  funcionário? '))
valor = valor = sal + (sal * 15 / 100)
if sal > 1250:
    valor = sal + (sal * 10 / 100)   
print(f'Quem ganhava R$ {sal} passa a ganhar R${valor:.2f}')
