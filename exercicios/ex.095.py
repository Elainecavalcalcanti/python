jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    
    time.append(jogador.copy())   # corrigido
    
    while True:
        resp = str(input('Quer Continuar [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if resp == 'N':
        break

print('-=' * 40)
print(f'{"cod":<5}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():   # corrigido
        print(f'{str(d):<15}', end='')
    print()

print('-=' * 40)

print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    
    if busca == 999:
        break
    
    if busca >= len(time):
        print('ERRO! Jogador não existe.')
    else:
        print(f'Levantamento do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')


