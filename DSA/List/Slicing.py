# Accessing and modifying several elements from objects such as lists/tuples/strings 
# requires using a for loop in most languages. However, in Python, you can use square brackets
# and a colon to define a range of elements within a list that you want to access or ‘slice’.

list1 = [1,2,3,4,5,5,6,77,7,11,88,8,]
print(list1)

# list[starting index: ] -> represent from given index to end index of list.
# list[ :ending index] -> from 0th index to given index. 
print(list[:]) # -> All the numbers in the range
print(list[1:6])


# Stepped Indexing 

# just like for loop 
print("Using For loop: ")
for i in range(0, 20, 2):
    print(i)

print("Using Slice: ")

# list[start :  stop :  step(basically to skip how many element after a element)]

# 1 is default step for every slice function 
# 2 is for skipping the one element
print(list1[0:9:2])
print(list1[9: 0])  # if we didn't define step in this case it will return empty list
print(list1[9: 0: -2]) # now after step parameter it will give list from (9th to 0th) index with skipping 1 element
#  Reverse a list using slice
print(list1[ : 0 : -1])


# Intialize new element using slice

x = list(range(5))
print(x)

x[1:4] = [23,34,56]

print(x)


