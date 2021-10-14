memo = {}


def fib(n):
  if n in memo:
      return memo[n]
  if n <= 1:
      return 1

  memo[n] = fib(n - 1) + fib(n - 2)
  return memo[n]

  # return fib(n - 1) + fib(n - 2)


for x in range(101):
  print(x, ":", fib(x))
