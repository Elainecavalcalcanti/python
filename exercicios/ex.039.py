from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')

if idade  <  18:
    faltam= 18 - idade
    ano = ano_atual + faltam
    print(f'Ainda Faltam {faltam} anos para o alisatamento')
    print(f'Seu alistamento será em {ano}.')

elif idade > 18:
    passou = idade - 18
    ano = ano_atual - passou
    print(f'Voce ja deveria ter se alistado há {passou} anos.')
    print(f'Seu alistamento foi em {ano}.')

else:
    print(f'Seu alistamento é esse ano!')
