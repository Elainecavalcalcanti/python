palavras = ('aprender', 'programar', 'linguagem', 'Ppython', 'curso',
            'gratis', 'estuddar', 'praticar', 'trabalhar', 'mercado')

for p in palavras:
    # Adicionamos o end='' para as vogais virem logo em seguida
    print(f'Na palavra {p.upper()} temos ', end='') 
    
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            
    # Esse print sozinho serve apenas para pular a linha para a PRÓXIMA palavra
    print()