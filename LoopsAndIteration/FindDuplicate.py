def checkDuplicate(list):

    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                 return True
    return False


list = [1,2,43,5,6,78,9990,0]
print(checkDuplicate(list))
       
      
       
    
  


