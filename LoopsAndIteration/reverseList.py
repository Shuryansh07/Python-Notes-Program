def toReverseList(list):
    new_list = []
    for i in range(1, len(list) + 1):
        new_list.append(list[-i])
    return new_list

def toReverseList2(list):
    size = len(list)
    s = size 
    new_list = [None] * size

    for i in list:
        s = s - 1
        new_list[s] = i
    return new_list

list = [1, 2,3,4,54,5,7]
reversed_list = toReverseList(list)
reversed_list2 = toReverseList2(list)
print(reversed_list)
print(reversed_list2)



