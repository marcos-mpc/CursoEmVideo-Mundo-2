num = int(input('digite um numero inteiro: '))
print(''''escolha a base para converção :
[ 1 ] para binario
[ 2 ] para octal
[ 3 ] para hexadecimal''')
opção = int(input('digite sua escolha : '))
if opção == 1:
    print('{} convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida. tente novamente !')
