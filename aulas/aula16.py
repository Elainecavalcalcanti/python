lanche = ('Hamburguer','Suco','Pizza','Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-'*20)
for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')
print('-'*20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')