# sum of first 10 numbers
#
# odd even
#
# find largest number in a list
#
# largest of 3 numbers by taking variables
#
# processor name and system name using python
#
# sorting in a list
#
# square root of a number
#
# sum of elements in a list
#
# groupby
#
# primary key
#
# Dense Layer

import platform
import math


def sumof(n):
    return n(n + 1) / 2


def odd_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def largest(arr):
    return arr.max()


def max_3(a, b, c):
    if c < a > b:
        return c
    elif a < b > c:
        return b
    elif a < c > b:
        return c
    else:
        print('Numbers are not Identical')


def machine_info():
    print('The Processor is:', platform.processor())
    print('The System is', platform.system())


def sort_arr(arr):
    return arr.sort()


def squareroot(x):
    return math.sqrt(x)

def sum_list(arr):
    return sum(arr)

