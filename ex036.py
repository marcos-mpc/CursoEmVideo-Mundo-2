print(10*'\033[33m=-')
print('\033[34mAPROVANDO EMPRESTIMO')
print(10*'\033[33m=-\033[m')
valor = float(input('digite o valor da casa: R$'))
salario = float(input('digite o valor de seu salario: R$'))
anos = float(input('digite em quantos anos vc pretende pagar: '))
meses = anos * 12
prestacao = valor / meses
if prestacao > 30 * salario / 100:
    print('lamento, mas seu emprestimo foi negado!')
else:
    print('parabens! seu emprestimo foi aprovado!')
