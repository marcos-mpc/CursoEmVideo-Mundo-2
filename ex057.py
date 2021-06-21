sexo = ''
while sexo != 'M' and sexo != 'F':
    s = input('qual seu sexo M/F ? ').strip() .upper()
    sexo = s
    if s != 'M' and sexo != 'F':
        print('OPÇÃO INCORRETA, TENTE NOVAMENTE !')
