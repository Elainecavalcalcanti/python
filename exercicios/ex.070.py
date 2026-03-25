totcompra = maior = menor = cont = 0
barato = ' '
print('-'*40)
print('          LOJAO SUPER URACH')
print('-'*40)
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Preco R$ '))
    cont += 1
    totcompra += valor
    if valor > 1000:
        maior+= 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('--------FIM DO PROGRAMA--------')
print(f'O total da compra foi R${totcompra}')
print(f'Temos {maior} produto custando mais de R$ 1000.00')
print(f'O produto mais barato foi a {barato} que custa R${menor:.2f}')
