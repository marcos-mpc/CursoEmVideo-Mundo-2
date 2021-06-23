print(13 * '\033[96m*-')
print('\033[97m CONDIÇÕES DE PAGAMENTO')
print(13 * '\033[96m*-\033[m')
preco = float(input('digite o valor do produto: '))
condicao = int(input('agora selecione a forma de pagamento\n'
                     '\033[93m1\033[33m à vista dinheiro/cheque\n'
                     '\033[93m2\033[33m à vista no cartaõ\n'
                     '\033[93m3\033[33m em até 2x no cartão\n'
                     '\033[93m4\033[33m 3x ou mais no cartão\n\033[m'))
if condicao == 1:
    atual = preco - preco * 10 / 100
    escolha = 'com 10% de desconto'
elif condicao == 2:
    atual = preco - preco * 5 / 100
    escolha = 'com 5% de desconto'
elif condicao == 3:
    atual = preco
    escolha = 'em até 2x no cartão nao tem alteração, então'
elif condicao == 4:
    atual = preco + preco * 20 / 100
    escolha = 'com 20% de juros'
else:
    print('opção invalida. tente novamente!')
    atual = preco
    escolha = preco
print('o valor de R${:.2f}, {},o valor atual fica {:.2f}'.format(preco, escolha, atual))
