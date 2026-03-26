lista = []
def media_aluno(nome,nota1,nota2):
    media = (nota1 + nota2) / 2
    print(f'O aluno {nome} teve média {media}')

for c in range(0,3):
    nome = str(input('Nome: '))
    nota1 = float(input(f'Primeira nota de {nome}: '))
    nota2 = float(input(f'Segunda nota de {nome}: '))
    media_aluno(nome, nota1,nota2)
    lista.append(media_aluno)

print(lista)