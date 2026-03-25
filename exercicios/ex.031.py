km = float(input('Qual a distancia da sua viagem? '))
print(f'Voce está prestes a comecar uma viagem de {km} km.')
if km >= 200:
    valor = km * 0.45
else:
    valor = km * 0.50

print(f'E o valor dda sua passagem é R${valor}')
