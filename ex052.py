print(10*'\033[30m-_')
print('\033[90mNUMEROS PRIMOS')
print(10*'\033[30m-_\033[m')
n = int(input('digite um numero: '))
if n % n == 0 and n % 1 == 0 and n % 2 != 0:
    print('esse numero é um numero primo')
else:
    print('esse numero nao é numero primo')
