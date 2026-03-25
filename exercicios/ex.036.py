ValorCasa= float(input('Valor da casa: R$ '))
Salario= float(input('Salário do comprador: R$ '))
anos=int(input('Quantos anos de financiamento? '))

Quantidade_parcelas = anos * 12
ValorParcelas = ValorCasa / Quantidade_parcelas

minimo = Salario * 30 / 100

print(f'Para Pagar uma casa de R${ValorCasa:.2f} em {anos} a prestacao será de R ${ValorParcelas:.2f}')

if ValorParcelas <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')

else:
    print('Emprestimo NEGADO!')