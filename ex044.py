print(13 * '\033[96m*-')
print('\033[97m CONDIÇÕES DE PAGAMENTO')
print(13 * '\033[96m*-\033[m')
preço = float(input('digite o valor do produto: '))
condição = int(input('agora selecione a forma de pagamento\n'
                     '\033[93m1\033[33m à vista dinheiro/cheque\n'
                     '\033[93m2\033[33m à vista no cartaõ\n'
                     '\033[93m3\033[33m em até 2x no cartão\n'
                     '\033[93m4\033[33m 3x ou mais no cartão\n\033[m'))
if condição == 1:
    atual = preço - preço * 10 / 100
    escolha = 'com 10% de desconto'
elif condição == 2:
    atual = preço - preço * 5 / 100
    escolha = 'com 5% de desconto'
elif condição == 3:
    atual = preço
    escolha = 'em até 2x no cartão nao tem alteração, então'
elif condição == 4:
    atual = preço + preço * 20 / 100
    escolha = 'com 20% de juros'
else:
    print('opção invalida. tente novamente!')
    atual = preço
    escolha = preço
print('o valor de R${:.2f}, {},o valor atual fica {:.2f}'.format(preço, escolha, atual))
