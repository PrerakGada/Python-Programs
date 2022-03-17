memo = {}


def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
    # Uncomment next line and comment the above 2 lines for a normal recursion approach
    # return fib(n - 1) + fib(n - 2)


for x in range(int(input('Enter the Length of Fibonacci Series: '))):
    print(x, ":", fib(x))
