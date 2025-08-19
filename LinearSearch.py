def LinearSearch(l1,x,index):
    if len(l1)==index:
        return False
    
    anslist=LinearSearch(l1,x,index+1)

    if anslist==True:
        return True
    
    if l1[index]==x:
        return True
    return False

print(LinearSearch([1,2,3,4,5,6],7,0))
