cont = acul = maior = menor = 0
fim = 'S'
while fim == 'S':
    n = int(input('digite um numero: '))
    cont += 1
    acul += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    fim = input('digitar outro numero ? S/N ').strip().upper()[0]
média = acul / cont
print('''a media dos valores digitados foi {:.2f}
o maior valor foi {}
o menor valor foi {}'''.format(média, maior, menor))
