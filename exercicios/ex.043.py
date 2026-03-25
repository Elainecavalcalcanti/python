peso = float(input('Qual é o seu Peso? (Kg) '))
altura = float(input('Qual a sua Altura? (m) '))

imc = peso / (altura ** 2 )
print(f'O IMC dessa pessoa é de {imc:.2f}')

if imc < 18.5:
    print('Voce está AABAIXO DO PESO normal')

elif 18.5 <= imc < 25:
    print('PARABENS, voce esta na faixa de PESO NORMAL')

elif 25 <= imc < 30:
    print('Voce está em sobrepeso')

elif 30 <= imc < 40:
    print('voce esta em Obesidade')
else:
    print('CUIDADO! Voce está Obesidade mórbida')

