def findFibonacci(x):
    if x == 1 or x == 2:
        return 1
    return findFibonacci(x - 2) + findFibonacci(x - 1)

print(findFibonacci(10))