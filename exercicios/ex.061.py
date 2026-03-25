print('GERADOR DE PA')
print('=-'*10)
primeiro = int(input('Primeiro termo: ')) #guarda primeiro numero da progressao
razao = int(input('RAZAO da PA: ')) # guardar valor da razao que sera somado a cada termo
termo =  primeiro  # o termo sera o primeiro quando eu difitar no 
cont = 1 # contar quantos termos ja foram mostrados
while cont <= 10: #enquando o contador for menor ou iogual a 10 ele vai continuar funcionando
    print(f'{termo} -> ', end=(' ') )
    termo += razao # o mesmo que termo = termo +  razao ou ex primeiro =3  razao 5  5 + 3 = 8 8 + 3 = 11 e assim vai
    cont += 1 # conta até chegar no while que menos igual a 10
print('FIM')
