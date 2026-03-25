print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # O ^ centraliza o texto
print('-' * 40)

lista = (
    ('Lápis', 1.75),
    ('Borracha', 2.00),
    ('Caderno', 15.90),
    ('Estojo', 25.00),
    ('Transferidor', 4.20),
    ('Compasso', 9.99)
)

for produto, valor in lista:
    # .:<30 significa: alinhe à esquerda (<), ocupe 30 espaços e preencha com ponto (.)
    print(f'{produto:.<30}R$ {valor:>7.2f}') 

print('-' * 40)