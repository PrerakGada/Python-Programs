import sys
from colorama import Fore, Back, Style
from colorama import init

init()


def printPos(x, y, text_to_print):  # Function that let us print in desired Position
    sys.stdout.write("\x1b[%d;%df%s" % (x, y, text_to_print))
    sys.stdout.flush()


print(Fore.RED + "Command >>")  # Red-colored print statement
printPos(1, 11, " ")  # Changing pos to 1, 11
inp = input()  # Getting the input
printPos(1, 11, inp)  # Changing pos to 1, 11
