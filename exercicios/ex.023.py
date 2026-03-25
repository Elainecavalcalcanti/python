num=int(input('Informe um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 100 % 10
print(f'Analisando o número {num}')
print(f'Unidade {u}')
print(f'dezena {d}')
print(f'centena {c}')
print(f'milhar {m}')