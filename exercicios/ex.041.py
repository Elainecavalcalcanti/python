from datetime import date
ano_atual = date.today().year

data = int(input('Ano de Nascimento: '))

idade= ano_atual - data
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificacao: MIRIM')
elif idade <=14:
    print('Classificacao: INFANTIL')
elif idade <=19:
    print('Classificacao: JUNIOR')
elif idade <=25:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')
