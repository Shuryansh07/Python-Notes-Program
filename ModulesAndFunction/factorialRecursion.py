def findFactorial(x):
    if x == 1:
        return 1
    return x * findFactorial(x - 1)


print(findFactorial(11))
print(findFactorial(5))