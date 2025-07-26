a = [1,2,3,4,5,6]

print(a)
print(a[0])
print(a[1])

# SubList(list Slicing)
a1 = a[0:3]
print(a1)

b1 = a[3:6]
print(b1)

# Concatanation
aConcated = a1 + b1
print(aConcated)

# Traversal
for val in a:
    print(val)