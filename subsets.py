def subsets(nums):
    results = [[]]
    for i in nums:
        results += [
            item + [i]
            for item in results
        ]
    return results
  
print(subsets([10, 20, 30]))
