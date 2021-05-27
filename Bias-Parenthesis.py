from Stack import *


def bias_parenthesis(e):
    s = Stack()
    for x in e:
        if x == '(':
            s.push(x)
        elif x == "[":
            s.push(x)
        elif x == "{":
            s.push(x)

        elif x == ')':
            if s.peek() == '(':
                s.pop()
            else:
                return print('Unbiased')
        elif x == "]":
            if s.peek() == '[':
                s.pop()
            else:
                return print('Unbiased')
        elif x == "}":
            if s.peek() == '{':
                s.pop()
            else:
                return print('Unbiased')

    return print('Biased')


# Driver Code

equation = input("Enter an Equation: ")
bias_parenthesis(equation)
