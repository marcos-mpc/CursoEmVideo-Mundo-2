frase = input('digite uma frase: ').strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for a in range(len(junto)-1, -1, -1):
    inverso += junto[a]
print('a frase {} invertida fica {}'.format(junto, inverso))
if junto == inverso:
    print('temos um palindromo')
else:
    print('nao temos um palindromo')
