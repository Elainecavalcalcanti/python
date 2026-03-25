print('========= LOJAS GUABANARA =========')
compra = float(input('Preco das Compras: R$'))
print( '''FORMAS DE PAGAMENTO
      [ 1 ] À vista dinheiro/pix
      [ 2 ] À vista cartao
      [ 3 ] 2x no cartao
      [ 4 ] 3x ou mais no cartao''')
opcao=int(input('Qual é a sua opcao? '))

if opcao == 1:
    desconto = compra - (compra * 10/100)
    print(f'Sua Compra de R${compra} vai custar R${desconto:.2f} no final.')

elif opcao == 2:
    desconto = compra - (compra * 5/100)
    print(f'Sua compra de R${compra} vai custar R${desconto:.2f} no final')

elif opcao == 3:
    parcela = compra / 2 
    print(f'Sua compra será parcelada em 2x de {parcela:.2f}')
    print(f'Sua compra de R${compra} vai custar R${valor} no final')

elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = compra + (compra * 20/100 )
    quant_parcela= juros / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de {quant_parcela} COM JUROS ')
    print(f'Sua compra de R${compra} vai custar R${juros} no final.')
    
else:
    print('Opcao invalida')
