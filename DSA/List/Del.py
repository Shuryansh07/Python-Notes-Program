list1 = [1,2,3,4,5,5,6,7,7,8,8,8,98,9]

print(list1)
# Using del together with slice we deleted every even index 0th , 2th, ..(element) from list
del list1[::2]

print(list1)

# Delete all element
del list1[:]
print(list1)