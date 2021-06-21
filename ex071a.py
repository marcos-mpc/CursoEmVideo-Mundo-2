n = int(input('digite quanto a ser sacado: '))
total = n
ced = 50
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'total de {cont} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break