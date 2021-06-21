n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
escolha = 0
while escolha != 5:
    print(22*'\033[93m=')
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    print(22*'\033[93m=\033[m')
    escolha = int(input('digite sua escolha: '))
    if escolha == 1:
        print('\033[91ma soma entre os numeros {} e {} é igual à {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('\033[91mo resultado de {} x {} é igual à {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('\033[91mo maior numero é %s' % n1)
        else:
            print('\033[91mo maior numero é %s' % n2)
    elif escolha == 4:
        n1 = float(input('primeiro numero: '))
        n2 = float(input('segundo numero: '))
    else:
        print('\033[91mOPÇÃO INVALIDA! TENTE NOVAMENTE')
print('\033[91mPROGRAMA ENCERRADO')
