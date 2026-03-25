import math
opo = float(input('Comprimento ddo cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente:'))
hipo = (opo ** 2 + adj ** 2)
tot = math.sqrt(hipo)
print(f'A hipotenusa vai medir {tot:.2f}')
