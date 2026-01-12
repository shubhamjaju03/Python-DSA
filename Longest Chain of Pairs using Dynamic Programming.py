def FindLargestChain(pairs):
    n=len(pairs)
    dp = [1]*n
    pairs.sort()
    longest_chain = 1
    for i in range(1,n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
        if dp[i]> longest_chain:longest_chain=dp[i]
    return longest_chain

pairs = [(5, 24), (15, 25), (27, 40), (50, 60)]

result = FindLargestChain(pairs)
print(result)
