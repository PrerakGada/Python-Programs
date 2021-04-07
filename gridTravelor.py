memo = {}


def gridTraveler(m, n):
    key = f'{m},{n}'
    if key in memo:
        return memo[key]
    if m == n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    return memo[key]


print(gridTraveler(3, 3))
print(gridTraveler(5, 5))
print(gridTraveler(10, 10))
print(gridTraveler(15, 15))
print(gridTraveler(20, 20))
