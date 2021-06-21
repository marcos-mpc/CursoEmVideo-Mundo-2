from time import sleep
print(7*'\033[32m=-=')
print('\033[31mCONVERSOR DE BASES')
print(7*'\033[32m=-=\033[m')
numero = int(input('digite um numero inteiro: '))
print('escolha qual das bases vc quer converter esse valor ?')
escolha = int(input('\033[31m 1\033[m para binario\n\033[31m 2\033[m para octal\n\033[31m 3 \033[mpara hexadecimal\n '))
print('PROCESSANDO...')
sleep(2)
if escolha == 1:
    print('numero binario')
elif escolha == 2:
    print('numero octal')
elif escolha == 3:
    print('numero hexadecimal')
