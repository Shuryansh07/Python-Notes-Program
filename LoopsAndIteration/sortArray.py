def isSort(list):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            return False
    return True


list = [1,3,4,5,6,7,8,9]

print(isSort(list))
