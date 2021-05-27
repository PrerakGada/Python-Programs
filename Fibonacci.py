memo = {}


def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


for x in range(51):
    print(x, ":", fib(x))
