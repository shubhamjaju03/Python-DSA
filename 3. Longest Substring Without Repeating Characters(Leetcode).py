def max_unique_length(str):
    char_index = {}
    left = 0
    max_length = 0
        
    for right in range(len(str)):
        if str[right] in char_index:
            left = max(left, char_index[str[right]] + 1)
        
        char_index[str[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
