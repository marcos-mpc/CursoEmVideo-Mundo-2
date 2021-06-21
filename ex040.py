print(10*'\033[30m=-')
print('\033[31mCALCULO DE MEDIA')
print(10*'\033[30m=-\033[m')
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[31mVC FOI REPROVADO !')
elif media >= 7:
    print('\033[32mVC FOI ARPOVADO !')
else:
    print('\033[33mVC ESTA DE RECUPERAÇÃO !')
print('sua media foi {:.1F} o necessario para ser aprovado era {}'.format(media, 7.0))