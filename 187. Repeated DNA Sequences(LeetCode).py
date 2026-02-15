def findRepeatedDnaSequences(s):
    L = 10
    if len(s) < L:
        return []
    
    seen = set()
    repeated = set()
    
    for i in range(len(s) - L + 1):
        substring = s[i:i+L]
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)
    return list(repeated)
