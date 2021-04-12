# 1
"""
x = int(input('X: '))
y = int(input('Y: '))
z = int(input('Z: '))

if x == y == z:
    print('Equilateral')
elif x == y or y == z or x == z:
    print('Isosceles')
else:
    print('Scalene')
"""

# 2
"""
x = 0
while x <= 50:
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

    x += 1
"""

# 3
"""
x = 1
n = int(input('Input a number: '))
while x <= 10:
    print(f'{n} x {x} = {n * x}')

    x += 1
"""


# 4

def operations(x):
    a = int(input('Enter 1st Number: '))
    b = int(input('Enter 2nd Number: '))

    switcher = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b
    }

    return switcher.get(x, 'Invalid')


print(operations(input('Enter the Operation: ')))
