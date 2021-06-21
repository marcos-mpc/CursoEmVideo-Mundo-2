from datetime import date
print(20*'\033[32m=')
print('\033[92mMAIOR IDADE')
print(20*'\033[32m=\033[m')
contmaior = 0
contmenor = 0
atual = date.today().year
for c in range(0, 7):
    n = int(input('em que ano vc nasceu ? '))
    if atual - n < 21:
        contmenor += 1
    else:
        contmaior += 1
print('tem {} que sao maior de idade'.format(contmaior))
print('tem {} que são menor de idade'.format(contmenor))
