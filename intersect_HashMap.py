def intersect(num1, num2):
    hashmap = {}
    ans = []
    
    for i in num1:
        hashmap[i] = True
    
    for j in num2:
        if j in hashmap:
            ans.append(j)
    
    return ans
num1 = [1, 2, 3, 4]
num2 = [2, 4, 6, 8]
print(intersect(num1, num2))
