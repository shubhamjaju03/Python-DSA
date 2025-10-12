def contains_duplicates(num1, num2):
    hashmap = {}
    ans = []
    
    for i in num1:
        hashmap[i] = True
    
    for j in num2:
        if j in hashmap and j not in ans:
            ans.append(j)
    
    return ans
num1 = [1, 2, 3, 4,5]
num2 = [2, 4, 6, 8,5]
print(f"These numbers are duplicate in list {num1}, {num2}: {contains_duplicates(num1, num2)}")
