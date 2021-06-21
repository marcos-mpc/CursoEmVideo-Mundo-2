n = int(input('digite um numero: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        total += +1
    else:
        print('\033[33m', end=' ')
    print(c, end=' ''\033[m')
if total == 2:
    print('\nseu numero é divisivel por {} vezes e ele é um numero primo'.format(total))
else:
    print('\nseu numero é didivivel por {} vezes e ele nao é um numero primo'.format(total))
