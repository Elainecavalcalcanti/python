print('=' * 25)
print('   10 TERMOS DE UMA PA')
print('=' * 25)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(c, end=(' -> '))


print('ACABOU')
