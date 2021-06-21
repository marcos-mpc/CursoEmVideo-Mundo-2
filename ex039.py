from datetime import date
print(20*'\033[32m=')
print('\033[30mALISTAMENTO MILITAR')
print(20*'\033[32m=\033[m')
ano = int(input('digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print('\033[33m esse ano vc tem que se alistar')
elif idade == 19:
    print('\033[33mjá passou a data de seu alistamento')
elif idade == 17:
    print('\033[33mano que vem é o ano de seu alistamento')
elif idade < 17:
    print('\033[33mainda falta muito tempo para seu alistamento')
elif idade > 19:
    print('\033[33mja faz um bom tempo desde seu alistamento\nespero que vc ja tenha se alistado!')
