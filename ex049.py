print(4*'\033[94m*-')
print('\033[96mTABUADA')
print(4*'\033[94m*-\033[m')
n = int(input('digete um numero: '))
for c in range(0, 10 + 1):
    print('{} x {} = {}'.format(n, c, n*c))
