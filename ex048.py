print(15*'\033[93m-=')
print('\033[95mSOMANDO IMPARES MULTIPLOS DE 3')
print(15*'\033[93m-=\033[m')
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print('a soma de todos os numeros impares multiplos de 3 de 1 a 500 é {}'.format(s))
