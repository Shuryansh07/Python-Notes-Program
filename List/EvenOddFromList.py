def evenOddList(n):
    l1 = [[x for x in range(0,n + 1) if x % 2 == 0], [x for x in range(0, n + 1) if x % 2 == 1]]
    return l1

print(evenOddList(10))