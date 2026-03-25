jogador = {}
gol = []

tot= 0

jogador['Nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {jogador["Nome"]} jogou? ')) 

for i in range(0,quant):
    gol_partida = int(input(f'Quantos gols na partida {i+1}? '))
    gol.append(gol_partida)
    tot = tot + gol_partida


jogador['gols'] = gol
jogador['total'] = tot

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {quant} partidas.')
for i, g in enumerate(gol):
    print(f'Na partida {i+1}, fez {g} gols')