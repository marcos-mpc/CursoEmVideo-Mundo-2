print(20*'\033[31m*')
print('\033[91mPALINDROMO')
print(20*'\033[31m*\033[m')
frase = input('digite uma frase: ')
esp = frase.split()
jun = ''.join(esp)
quan = len(jun)
for c in jun:
    print(c)
