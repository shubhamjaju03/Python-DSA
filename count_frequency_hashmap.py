def count_frequency(nums):
    ans={}
    for eachNumber  in nums:
        if eachNumber in ans:
            ans[eachNumber]+=1
        else:
            ans[eachNumber]=1
    return ans
        
nums=(1,2,2,3,4,5,6,6)
print(count_frequency(nums))
