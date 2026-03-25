n1 = float(input('Primeira Nota: ')) #Primeira Nota
n2 = float(input('Segunda Nota: '))  #Segunda Nota

#Calculo da media
media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, a média do aluno é {media}.')
#Condicoes 

if media < 5:
    print('O aluno está REPROVADO ')

elif 5 <= media <= 6.9:
    print('O aluno está em  RECUPERACAO')
elif media > 7:
    print('O aluno está APROVADO.')