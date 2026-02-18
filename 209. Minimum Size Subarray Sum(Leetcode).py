def minSubArrayLen(target, nums):
    left = 0
    total = 0
    min_length = float('inf')
    
    right = 0
    
    while right < len(nums):
        total = total + nums[right]
        
        while total >= target:
            curr_length = right - left
            curr_length = curr_length + 1
            
            if curr_length < min_length:
                min_length = curr_length
                
            total = total - nums[left]
            left = left + 1
        
        right = right + 1
    
    if min_length == float('inf'):
        return 0
    
    return min_length
