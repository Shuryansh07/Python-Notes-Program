def AppendElement(l):
    a = 90
    l.append(a) # This will append element in original List
    return l

def AppendElement2(l):
    a1 = 45
    l = l + [a1] # This will create a new duplicate list 
    return l


l = [1,2,3,4,5,67,78]


AppendElement(l)
print(l)
l = AppendElement2(l)  # Thats why we need to assign in l
print(l)