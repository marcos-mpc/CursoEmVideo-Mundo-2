frase = input('digite uma frase: ').strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = junto[::-1]
print('a frase {} invertida fica {}'.format(junto, inverso))
if junto == inverso:
    print('temos um palindromo')
else:
    print('nao temos um palindromo')
