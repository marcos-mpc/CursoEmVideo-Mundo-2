print(23*'\033[92m=')
print('\033[93m EXAMINANDO TRIANGULOS')
print(23*'\033[92m=\033[m')
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))
if r1 + r2 >= r3 and r2 + r3 >= r1 and r1 + r3 >= r2:
    print('\033[33mforma um triangulo')
else:
    print('\033[33mnao forma um triangulo')
if r1 == r2 == r3:
    triangulo = 'equilatero'
elif r1 == r2 > r3 or r2 == r3 > r1 or r1 == r3 > r2:
    triangulo = 'esósceles'
elif r1 != r2 != r3:
    triangulo = 'escaleno'
print('\033[32msuas retas formam um triangulo {}'.format(triangulo))
