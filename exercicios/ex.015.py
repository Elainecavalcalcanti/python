dias=int(input('Quantos dias alugados? '))
km = float(input('Quantos Km roddados? '))
totd=dias*60
totk=km*0.15
total=totd + totk
print(f'O total a pagar é R${total}')