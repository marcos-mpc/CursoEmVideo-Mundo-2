print(10*'\033[94m-_')
print('\033[95mCALCULO DE IMC')
print(10*'\033[94m-_\033[m')
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    status = 'abaixo do peso'
elif 18.5 < imc <= 25:
    status = 'peso ideal'
elif 25 < imc <= 30:
    status = 'sobrepeso'
elif 30 < imc <= 40:
    status = 'obesidade'
else:
    status = 'obesidade morbida'
print('seu imc é \033[95m{:.1f}\033[m e seu status é \033[95m{}\033[m'.format(imc, status))