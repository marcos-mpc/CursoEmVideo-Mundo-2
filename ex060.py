n = int(input('digite um numero: '))
m = n
for c in range(n - 1, 0, -1):
    mult = m * c
    m = mult
print('o fatorial de {}! = {}'.format(n, m))
