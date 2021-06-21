from datetime import date
print(20*'\033[90m*')
print('\033[91mCATEGORIA DE NATAÇÃO')
print(20*'\033[90m*\033[m')
ano = int(input('digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 10:
    categoria = 'mirim'
elif 9 < idade < 15:
    categoria = 'infantil'
elif 14 < idade < 19:
    categoria = 'junior'
elif 18 < idade < 21:
    categoria = 'senior'
elif idade > 20:
    categoria = 'master'
print('\033[93mcom {} anos, sua categoria é nadador {}'.format(idade, categoria))
