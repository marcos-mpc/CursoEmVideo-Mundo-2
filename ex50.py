print(11*'\033[95m*_')
print('\033[97mSOMA DE NUMEROS PARES')
print(11*'\033[95m*_\033[m')
s = 0
for c in range(0, 6):
    n = int(input('digite um numero: '))
    if n % 2 == 0:
        s += n
print('a soma de todos os numeros pares é igual à {}'.format(s))
