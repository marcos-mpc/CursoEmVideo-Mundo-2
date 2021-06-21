cont = 0
acum = 0
fim = 0
while fim != 999:
    n = int(input('digite um numero (999 para encerrar): '))
    if n != 999:
        cont += 1
        acum += n
    fim = n
print('foram digitados {} numeros e a soma de todos eles é {}'.format(cont, acum))
