media = 0
maioridadehomem = 0
nomemaisvelho = ''
quantidademulher20 = 0
for c in range(1, 5):
    print('------{}ª pessoa ------'.format(c))
    nome = input('nome: ')
    idade = int(input('idade '))
    sexo = input('sexo M/F: ')
    media += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    elif sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        quantidademulher20 = 1
print('a media da idade do grupo é {}'.format(media / 4))
print('o homem mais velho é {} e ele tem {} anos'.format(nomemaisvelho, maioridadehomem))
print('{} mulher é menor que 20 anos'.format(quantidademulher20))
