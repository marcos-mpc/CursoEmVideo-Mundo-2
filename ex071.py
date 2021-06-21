from time import sleep
valor = int(input('digite o valor a ser sacado:R$ '))
cinq = valor
cont = cont2 = cont3 = cont4 = 0
while True:
    cinq -= 50
    cont += 1
    if cinq <= 0:
        break
if cinq < 0:
    cinq += 50
    cont -= 1
vint = cinq
while True:
    vint -= 20
    cont2 += 1
    if vint <= 0:
        break
if vint < 0:
    vint += 20
    cont2 -= 1
dez = vint
while True:
    dez -= 10
    cont3 += 1
    if dez <= 0:
        break
if dez < 0:
    dez += 10
    cont3 -= 1
um = dez
while True:
    um -= 1
    cont4 += 1
    if um <= 0:
        break
if um < 0:
    um += 1
    cont4 -= 1
print('AGUARDE. CONTANDO NOTAS...')
sleep(3)
print(f'\033[42;30mR$50,00\033[m = {cont}')
sleep(1)
print(f'\033[42;30mR$20,00\033[m = {cont2}')
sleep(1)
print(f'\033[42;30mR$10,00\033[m = {cont3}')
sleep(1)
print(f'\033[42;30mR$1,00 \033[m = {cont4}')
sleep(1)
print('PROGRAMA FINALIZADO!')
