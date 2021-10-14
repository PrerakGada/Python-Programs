import random
import numpy as np
from tabulate import tabulate
from colorama import Fore


def getTickets():
  ticket_list = np.zeros((3, 9), dtype=int)
  total_numbers = [num for num in range(1, 90)]
  total_indices = [(i, j) for i in range(3) for j in range(9)]
  random_indices = []

  first_row = random.sample(total_indices[:9], 5)
  second_row = random.sample(total_indices[9:18], 5)
  third_row = random.sample(total_indices[-9:], 5)

  for i in first_row:
    random_indices.append(i)

  for i in second_row:
    random_indices.append(i)

  for i in third_row:
    random_indices.append(i)

  for num in random_indices:
    if num[1] == 0:
      number = random.choice(total_numbers[:10])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 1:
      number = random.choice(total_numbers[10:20])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 2:
      number = random.choice(total_numbers[20:30])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 3:
      number = random.choice(total_numbers[30:40])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 4:
      number = random.choice(total_numbers[40:50])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 5:
      number = random.choice(total_numbers[50:60])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 6:
      number = random.choice(total_numbers[60:70])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 7:
      number = random.choice(total_numbers[70:80])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0
    elif num[1] == 8:
      number = random.choice(total_numbers[80:89])
      ticket_list[num] = number
      total_numbers[total_numbers.index(number)] = 0

  for col in range(9):
    if ticket_list[0][col] != 0 and ticket_list[1][col] != 0 and ticket_list[2][col] != 0:
      for row in range(2):
        if ticket_list[row][col] > ticket_list[row + 1][col]:
          temp = ticket_list[row][col]
          ticket_list[row][col] = ticket_list[row + 1][col]
          ticket_list[row + 1][col] = temp

    elif ticket_list[0][col] != 0 and ticket_list[1][col] != 0 and ticket_list[2][col] == 0:
      if ticket_list[0][col] > ticket_list[1][col]:
        temp = ticket_list[0][col]
        ticket_list[0][col] = ticket_list[1][col]
        ticket_list[1][col] = temp

    elif ticket_list[0][col] != 0 and ticket_list[2][col] != 0 and ticket_list[1][col] == 0:
      if ticket_list[0][col] > ticket_list[2][col]:
        temp = ticket_list[0][col]
        ticket_list[0][col] = ticket_list[2][col]
        ticket_list[2][col] = temp

    elif ticket_list[0][col] == 0 and ticket_list[1][col] != 0 and ticket_list[2][col] != 0:
      if ticket_list[1][col] > ticket_list[2][col]:
        temp = ticket_list[1][col]
        ticket_list[1][col] = ticket_list[2][col]
        ticket_list[2][col] = temp

  return ticket_list


def getToken():
  token = random.choice(tokens)
  tokens.remove(token)
  return token


def checkTickets(t):
  for ticket in tickets:
    for row in range(3):
      for col in range(9):
        if str(ticket[row][col]) == str(t):
          print(str(ticket[row][col]), end=' ')


# Driver Code
tokens = []
for x in range(1, 90):
  tokens.append(x)

numberOfTickets = input('Enter the number of players: ')
tickets = []
for i in range(int(numberOfTickets)):
  ticket = getTickets()
  tickets.append(ticket)
for ticket in tickets:
  print(tabulate(ticket, tablefmt="fancy_grid", numalign="center"))
  print(ticket)
  # print()

for x in range(89):
  token = getToken()
  checkTickets(token)
  # for ticket in tickets:
  #     print(tabulate(ticket, tablefmt="fancy_grid", numalign="center"))
