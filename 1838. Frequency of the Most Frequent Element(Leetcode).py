def maxFrequency(nums, k):
    
    nums.sort()
    
    left = 0
    total = 0
    max_freq = 0
    right = 0
    
    while right < len(nums):
        
        total = total + nums[right]
        
        while (nums[right] * (right - left + 1) - total) > k:
            
            total = total - nums[left]
            left = left + 1
        
        current_window = right - left
        current_window = current_window + 1
        
        if current_window > max_freq:
            max_freq = current_window
        
        right = right + 1
    
    return max_freq
