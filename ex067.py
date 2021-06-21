from time import sleep
while True:
    n = int(input('digite um numero para saber sua tabuada: '))
    if n < 0:
        break
    print(20*'*')
    for t in range(1, 11):
        print(f'{n} x {t} = {n * t}')
    print(20*'*')
print('Fim do programa.')
sleep(2)
