def getCube(n):
    l = [x ** 3 for x in range(1, n + 1)]
    return l

print(getCube(10))