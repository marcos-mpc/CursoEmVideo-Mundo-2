termo = int(input('TERMO: '))
razao = int(input('RAZÃO: '))
cont = 0
while cont < 10:
    print(termo, end=' ')
    termo += razao
    cont += 1
