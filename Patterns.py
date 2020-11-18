def half_triangle_up():
    n = input('Enter the size of the pattern: ')
    n = int(n)
    for i in range(0, n):
        for j in range(0, i + 1):
            print('*', end=' ')
        print()


def half_triangle_down():
    n = input('Enter the size of the pattern: ')
    n = int(n)
    for i in range(n, -1, -1):
        for j in range(0, i):
            print("*", end=' ')
        print()


def triangle_up():
    n = input('Enter the size of the pattern: ')
    n = int(n)
    for i in range(n, -1, -1):
        for j in range(0, i):
            print("", end=' ')
        for k in range(0, n - i):
            print('*', end=' ')
        print()


def triangle_down():
    n = input('Enter the size of the pattern: ')
    n = int(n)
    for i in range(n, -1, -1):
        for j in range(0, n - i):
            print("", end=' ')
        for k in range(0, i):
            print('*', end=' ')
        print()


def diamond():
    n = input('Enter the size of the pattern: ')
    n = int(n)
    for i in range(n, -1, -1):
        for j in range(0, i):
            print("", end=' ')
        for k in range(0, n - i):
            print('*', end=' ')
        print()
    for i in range(n, -1, -1):
        for j in range(0, n - i + 1):
            print("", end=' ')
        for k in range(0, i - 1):
            print('*', end=' ')
        print()


def rectangle():
    l = int(input("Enter the Length of the pattern: "))
    b = input("Enter the Breadth of the pattern: ")
    b = int(b)
    for i in range(0, l):
        for j in range(0, b):
            print("*", end=' ')
        print()


c = 'y'
while c == 'y':
    print('Enter the following numbers to execute the corresponding pattern.')
    print('1. Half Triangle')
    print('2. Half Inverted Triangle')
    print('3. Full Triangle')
    print('4. Full Inverted Triangle')
    print('5. Diamond')
    print('6. Rectangle')

    choice = input("Enter your choice: ")
    choice = int(choice)
    if choice == 1:
        half_triangle_up()
    elif choice == 2:
        half_triangle_down()
    elif choice == 3:
        triangle_up()
    elif choice == 4:
        triangle_down()
    elif choice == 5:
        diamond()
    elif choice == 6:
        rectangle()
    else:
        print('Wrong Choice')
    print("Do you want to draw pattern again?")
    c = input("Enter 'y' for YES: ")
