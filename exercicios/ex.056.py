somaidade = 0 
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pess in range(1,5):
    print(f'-----{pess}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    somaidade += idade
    if pess ==1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1



mediaidade = somaidade/4
print(f'A media de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo sao {totmulher20} com menos de 20 anos.')
