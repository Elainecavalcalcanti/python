from datetime import date 
totmaior = 0
totmenor = 0
atual = date.today().year
for pess in range(1, 7+1):
    nasc=int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade =  atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1 
print(f'Ao todo tivemos {totmaior} pessoas maiores de idades.')
print(f'E tambem tivemos {totmenor} pessoas menores de idade.')