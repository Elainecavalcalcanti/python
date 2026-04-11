def aluno(nome="<desconhecido>", nota=0):
    print(f'O aluno {nome} tirou a nota {nota}.')




a = input('Nome do aluno: ')
n = input(f'Nota de {a}: ')

if n.isnumeric():
    n = int(n)
else:
    n = 0
if a.strip() == '':
    aluno(nota=n)
else:
    aluno(a, n)
