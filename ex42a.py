r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))
if r1 + r2 >= r3 and r2 + r3 >= r1 and r1 + r3 >= r2:
    print('\033[33mforma um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO !')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ESOSCELES')
else:
    print('\033[33mnao forma um triangulo')