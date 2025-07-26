def GetSumOfEvenSquare(n):
    l1 = [x ** 2 for x in range(0, n+1) if x % 2 == 0]
    return l1


def GetEvenSquareeNotDivisbleBy3(n):
    l1 = [x ** 2 for x in range(0, n+1) if (x % 2 == 0 and x % 3 != 0)]
    return l1

# Using Range Parameter

def GetEvenSquareNotDivisbleBy3(n):
    l1 = [x ** 2 for x in range(0, n + 1, 2) if (x % 3 != 0)]
    return l1

l2 = GetSumOfEvenSquare(20)
print(sum(l2))

l3 = GetEvenSquareeNotDivisbleBy3(20)
print(l3)
print(sum(l3))

l4 = GetEvenSquareNotDivisbleBy3(20)
print(l4)
print(sum(l4))
