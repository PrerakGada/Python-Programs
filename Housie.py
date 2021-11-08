import random


def bingo():
  n = int(input("How many tickets do you need: "))
  print('\n\nNote: "OO" signifies Empty Space\n\n')
  for n1 in range(n):
    tkt = [[' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO '],
           [' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO '],
           [' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ', ' OO ']]

    d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    l = []
    while 1 < 2:
      a = random.randint(1, 89)

      if a not in l:
        if d[int(a / 10)] < 3:
          l.append(a)
          d[int(a / 10)] += 1
          if len(l) == 15:
            break

    for x in l:
      x1 = int(x / 10)
      if int(x / 10) == 0:
        x2 = str(f' 0{str(x)} ')
      else:
        x2 = str(f' {str(x)} ')
      while 1 < 2:
        a = random.randint(0, 2)
        if tkt[a][x1] == ' OO ':
          tkt[a][x1] = x2
          break

    print(f"Ticket No. {n1 + 1}\n")
    for i in tkt:
      print(*i)
    print('\n\n\n')

  a = input('Press Enter to Quit')


bingo()
