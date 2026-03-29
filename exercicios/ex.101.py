
def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif idade >= 16 and idade <= 17: 
        return f'Com {idade} anos: VOTO FACULTATIVO!'
    elif idade >= 18 and idade <=70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos:VOTO FACULTATIVO!' 


ano_nasc = int(input('Ano de Nascimento: '))
print(voto(ano_nasc))

