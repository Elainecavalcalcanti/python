import random
al1=input('Primeiro aluno: ')
al2=input('Segundo aluno: ')
al3=input('Terceiro aluno: ')
al4=input('Quarto aluno:')
lista = [al1,al2,al3,al4]
sorteio = random.choice(lista)
print(f'O aluno escolhido foi {sorteio}')