# List comprehension is a concise way to create list. They consist of square brackets containing
# expresion followed by for Keyword , The result will be a list that follows the expression.

SquareList = [ x * x for x in [1,2,3,4,5]]

print(SquareList)
print(type(SquareList))

EvenList = [ x % 2  for x in  [1,2,3,4,5,6,7]]  # Does not get the result get expected but someWhat get the logic
# This will just return remainder of x divided by 2
print(EvenList)


#  Using Range Function

a = range(0,4)

SquareList2 = [x * x for x in range(0,4)]
print(SquareList2)

# if you want to print only evenElement 
# List Comprehensions with Conditional Statements
EvenList2 = [x for x in range(0,10) if x % 2 == 0]

# Here x * x is output Expression
#  x is variable
#  range(0,10) -> reference Sequence
# Predicate(optional) -> (x % 2 == 0)

print(EvenList2)


PairElements = [(x,y) for x in [1,2,5,6,7] for y in [7,8,3,4,5,1] if x != y]

print(PairElements)


# 2-D List Comprehension

matrix = [[1,2,3,4], 
          [5,6,7,8],
          [9,10,11,12]]

Transpose = [[row[i] for row in matrix] for i in range(4)]

# Transpose through list comprehension
# Outer loop starts, i = 0:
# The inner loop [row[0] for row in matrix] runs.
# It goes through each row of matrix and picks the element at index 0:
# From [1,2,3,4], it gets 1.
# From [5,6,7,8], it gets 5.
# From [9,10,11,12], it gets 9.
# The inner loop creates the list [1, 5, 9]. This becomes the first row of Transpose.
# Outer loop continues, i = 1:
# The inner loop [row[1] for row in matrix] runs.
# It goes through each row of matrix and picks the element at index 1:
# From [1,2,3,4], it gets 2.
# From [5,6,7,8], it gets 6.
# From [9,10,11,12], it gets 10.
# The inner loop creates the list [2, 6, 10]. This becomes the second row of Transpose.
# This process continues for i = 2 and i = 3.

print(Transpose)