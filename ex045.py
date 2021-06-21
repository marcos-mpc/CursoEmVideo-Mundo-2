import random
print(9*'\033[93m-_')
print('\033[91m JOGO DE JOKENPÕ')
print(9*'\033[93m-_\033[m')
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
jogador = input('escolha: ')
if pc == jogador:
    resultado = 'empatou !'
elif pc == 'pedra' and jogador == 'tesoura' or pc == 'papel' and jogador == 'pedra' or pc == 'tesoura' and jogador == 'papel':
    resultado = 'pc ganhou !'
else:
    resultado = 'jogador ganhou !'
print('o resultado foi \033[93m{} \033[mas escolhas foram:\n\033[94mjogador {}\n'
      '\033[95mpc {}'.format(resultado, jogador, pc))
