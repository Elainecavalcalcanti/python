
def ficha(nome=0,gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')



nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if nome.strip():
    ficha(gols = gols)
else:
    ficha(nome, gols)