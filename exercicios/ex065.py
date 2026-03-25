opcao = 's'
soma = cont = menor = maior = media = 0
while opcao in'Ss':
    num=int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
    cont  += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Voce digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor {menor}')
