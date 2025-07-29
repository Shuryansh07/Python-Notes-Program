def findMaximum(l):
    maximum = 0
    for x in l:
        maximum = max(maximum, x)
    return maximum

# We use enumerate to find the index that holds the maximum value
def findMaximumIndex(l):
    maximum = 0
    maxIndex = 0
    for i, x in  enumerate(l):
        if x > maximum:
            maximum = x
            maxIndex = i
    return maxIndex


list = [10,87,3,4,5,6,67,8,32,167,4,5,6,72232,53,1222]
print(findMaximum(list))
print(findMaximumIndex(list))