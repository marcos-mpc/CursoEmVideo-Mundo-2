cont = acul = 0
while True:
    print(35 * "=")
    n = int(input('digite um numero [999 para parar]:  '))
    if n == 999:
        break
    cont += 1
    acul += n
print(45*'=')
print(f'a soma dos {cont} numeros digitados é igual à {acul}')
print(45*'=')
