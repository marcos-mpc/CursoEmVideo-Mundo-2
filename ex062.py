termo = int(input('TERMO: '))
razao = int(input('RAZÃO: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos vc quer mostrar mais ? '))
