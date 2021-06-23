print(10*'=')
print('JOKENPO')
print(10*'=')
from time import sleep
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('qual a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('-='*11)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR GANHA!')
    elif jogador == 2:
        print('COMPUTADOR GANHA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHA!')
    elif jogador == 1:
        print('COMPUTADOR GANHA!')
    elif jogador == 2:
        print('EMPATE!')
