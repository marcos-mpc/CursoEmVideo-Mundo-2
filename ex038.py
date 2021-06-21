print(20*'\033[35m*')
print('\033[36mCOMPARANDO NUMEROS')
print(20*'\033[35m*\033[m')
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
if n1 > n2:
    print('\033[31m{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('\033[31m{} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('\033[31mos dois numeros são iguais!')
