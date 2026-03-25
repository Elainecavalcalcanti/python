
sexo=input('Informe seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MF':
    sexo=input('Dados inválido. Por favor Informe seu sexo:[M/F] ').strip().upper()[0]
    if sexo == 'F':
        print('Sexo FEMININO registrado com sucesso.')
    else:
        print('Sexo MASCULINO registrado com sucesso')
print('FIM')
    