import emoji
from time import sleep
print(20 * '\033[91m*')
print('\033[93mCONTAGEM REGRESSIVA')
print(20 * '\033[91m*\033[m')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(5 * '\033[91m:fireworks: \033[93m:sparkler:', use_aliases=True))
