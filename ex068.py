from random import randint
cont = 0
while True:
    comp = randint(1, 2)
    jog = int(input('digite um numero: '))
    soma = comp + jog
    escol = input('P/I: ').strip().upper()[0]
    if escol == 'P':
        if soma % 2 == 0:
            print('\033[92mvc ganhou! Parabens!')
            print('Jogue mais uma vez\033[m')
            cont += 1
        else:
            break
    elif escol == 'I':
        if soma % 2 != 0:
            print('\033[92mvc ganhou! Parabens!')
            print('Jogue mais uma vez\033[m')
            cont += 1
        else:
            break
print('\033[91mvc perdeu!')
print(f'\033[33mvc ganhou {cont} vezes!\033[m')
