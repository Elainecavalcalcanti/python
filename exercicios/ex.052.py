num = int(input('Digite um numero: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print(f'\nO número {num} foi divisível {tot} vezes')

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')