preco=float(input('Qual é o preco do produto?'))
des= preco - (preco * 5 / 100)
print(f'O produto que custava R${preco}, na promocao com desconto de 5% vai custar R${des:.2f}')