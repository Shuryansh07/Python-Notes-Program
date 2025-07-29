a_list = ['loo', 2, 'a']

def foo():
    print("Hello from foo")

another_list = [foo, a_list, 10, 'Hello']

print(another_list)

another_list[0]()


# Append Function

list1 = [1,3,4,56,67,8,89,9,66,555]

list1.append(100000)

print(list1)