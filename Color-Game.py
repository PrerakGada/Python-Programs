from colorama import Fore, Back, Style, Cursor
import random

print("Let's see how fast can you name the font colors!!\n\n")

colors = [Fore.GREEN, Fore.RED, Fore.BLUE, Fore.RESET]
colornames = ['BLUE', 'WHITE', 'RED', 'GREEN']

for x in range(10):
    for y in range(8):
        print(random.choice(colors) + random.choice(colornames), end=' ')
    print()

