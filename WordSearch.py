import random
from colorama import *

# Creating a random board
board = []
for x in range(15):
  i = ''
  for y in range(24):
    i += (chr(random.randint(65, 90)))
  board.append(i)

for x in board:
  for y in x:
    print(y, end=' ')
  print()

# Inserting Values
words = ['TIGER', 'ELEPHANT', 'CAT', 'DOG', 'DEER', 'GOAT', 'COW', 'LION', 'DRAGON', 'GIRAFFE', 'CHEETAH', 'LEOPARD',
         'MONKEY', 'HORSE', 'RABBIT']
word = words.copy()
new_board = []
for x in board:
  w = random.choice(words)
  words.remove(w)
  a = random.randint(0, 24 - len(w))
  r = x[a:a + len(w):1]

  x = x.replace(r, w)

  print(r, w)

  new_board.append(x)


def printboard():
  for x in new_board:
    for y in x:
      if y == '*':
        print(Fore.GREEN + y + Fore.RESET, end=' ')
      else:
        print(y, end=' ')
    print()


def check(c):
  for x in range(len(new_board)):
    if c in new_board[x]:
      guess.append(c)
      temp = new_board[x].replace(c, '*' * len(c))
      # temp = new_board[x].replace(c, Fore.BLUE + c + Fore.RESET)
      new_board[x] = temp
      return True
  return False


guess = []
count = 0
while sorted(guess) != sorted(word) and count < 5:
  printboard()
  print()
  c = input('Enter the name of the Animal: ').upper()
  ans = check(c)
  if not ans:
    print(Fore.RED + 'Wrong Guess!' + Fore.RESET)
    count += 1

if count == 5:
  print(Fore.RED + 'Game Over!' + Fore.RESET)
else:
  print(Fore.GREEN + 'Congrats, You Guess all the Animals!!' + Fore.RESET)
