idad = 0
idhom = 0
for t in range(1, 3):
    nome = str(input('qual o nome da %s pessoa ? ' % t))
    idade = int(input('olá %s, qual a sua idade ? ' % nome))
    sexo = str(input('''qual seu sexo ?
    digite [ 1 ] para homem
    digite [ 2 ] para mulher
    digite a escolha: '''))
    idad += idade
print('a media de idade do grupo é de {:.0f} anos'.format(idad / t))
