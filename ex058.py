from random import randint
computador = randint(0, 10)
print('estou pensando em um numero...')
jogador = int(input('qual numero estou pensando ? é entre 0  e 10. '))
cont = 1
while jogador != computador:
    jogador = int(input('voce errou, tente novamente: '))
    cont += 1
print('PARABENS! VOCE ACERTOU! foi preciso {} tentativas para voce acertar.'.format(cont))
