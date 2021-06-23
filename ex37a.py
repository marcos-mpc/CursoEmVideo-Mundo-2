print(30*'=')
print('CONVERSOR DE BASE NUMERICA')
print(30*'=')
num = int(input('digite um numero inteiro: '))
print(''''escolha a base para converção :
[ 1 ] para binario
[ 2 ] para octal
[ 3 ] para hexadecimal''')
opcao = int(input('digite sua escolha : '))
if opcao == 1:
    print('{} convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida. tente novamente !')
