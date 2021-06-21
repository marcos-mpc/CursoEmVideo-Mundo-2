soma = valormil = valormenor = cont = 0
nomemenor = ''
while True:
    print(30*'-')
    produto = input('digite o nome do produto: ')
    valor = float(input('digite seu valor:R$ '))
    cont += 1
    if valor >= 1000:
        valormil += 1
    soma += valor
    if cont == 1 or valor < valormenor:
        valormenor = valor
        nomemenor = produto
    print(30*'-')
    while True:
        cond = input('cadastrar novo produto ? [S/N]').strip().upper()[0]
        if cond in 'SN':
            break
    if cond == 'N':
        break
print('\033[31mPrograma Finalizado!')
print(f'''\033[33mO total gasto nas compras foi R${soma:.2f}
{valormil} Produtos custaram acima de R$1000
{nomemenor} foi o produto mais barato custando R${valormenor:.2f}''')
