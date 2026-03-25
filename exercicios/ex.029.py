velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade >   80:
    multa = (velocidade - 80) * 7
    print('MULTADO! voce excedeu o limite permitido que é de 80km/h')
    print(f'Voce deve pagar uma multa de R${multa}')

print(f'Tenha um bom dia! Dirija com seguranca!')
