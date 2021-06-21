print(3*'\033[96m*')
print('\033[98mP.A')
print(3*'\033[96m*')
t = int(input('termo: '))
r = int(input('rasão: '))
f = t*11
for c in range(t, f, r):
    print(c)
