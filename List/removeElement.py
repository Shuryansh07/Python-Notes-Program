def removeElements(l1, l2):
    for i in l2:
        l1.remove(i)
    return l1


l1 = [1,2,3,4,5,6,98,89,7]
l2 = [98,89]

print(removeElements(l1, l2))

print(l1)