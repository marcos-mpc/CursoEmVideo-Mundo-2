primeiro = int(input('primeiro termo: '))
rasao = int(input('razao: '))
decimo = primeiro + (10 - 1) * rasao
for c in range(primeiro, decimo + rasao, rasao):
    print(c, end=' ')
