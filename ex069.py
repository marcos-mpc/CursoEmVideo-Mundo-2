print(25*'=')
cont1 = cont2 = cont3 = 0
while True:
    idade = int(input('digite sua idade: '))
    if idade >= 18:
        cont1 += 1
    while True:
        sexo = input('digite seu sexo: [M/F] ').strip().upper()[0]
        if sexo in 'MF':
            break
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F':
        if idade < 20:
            cont3 += 1
    print(25*'=')
    while True:
        cond = input('cadastrar outra pessoa ? [S/N] ').strip().upper()[0]
        if cond in 'SN':
            break
    if cond == 'N':
        break
print('Programa Finalizado!')
print(f'''foram cadastrados {cont1} pessoas maiores de 18 anos
{cont2} homens foram cadastrados
{cont3} mulheres menores de 20 anos foram cadastradas''')
