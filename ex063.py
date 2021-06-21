n = int(input('digite um numero de termos que deseja ver: '))
cont = 2
t1 = 0
t2 = 1
print('{} - {} '.format(t1, t2), end='')
while n > cont:
    cont += 1
    t3 = t1 + t2
    print(' - %s' % t3, end='')
    t1 = t2
    t2 = t3
