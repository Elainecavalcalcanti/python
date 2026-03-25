from datetime import datetime

ficha = { }

ficha['Nome:'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
ano_atual = datetime.now().year
ficha['idade'] = ano_atual - ano
ficha['Ctps'] = int(input('Carteira de Trabalho (0 não tem):'))


if ficha['Ctps'] == 0:
    for k, v in ficha.items():
        print(f'- {k} tem o valor {v}')
else:
    ficha['Contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$ '))
    ficha['Aposentadoria'] = ficha['idade'] + ((ficha['Contratação'] + 35) - datetime.now().year )

    for k, v in ficha.items():
        print(f'- {k} tem o valor {v}')
print('-='*50)