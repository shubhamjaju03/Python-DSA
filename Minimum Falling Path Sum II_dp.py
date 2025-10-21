def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]

    for j in range(n):
        dp[0][j] = grid[0][j]
    
    for i in range(1, n):
        min1, min2 = float('inf'), float('inf')
        min1_index = -1
        for j in range(n):
            if dp[i-1][j] < min1:
                min2 = min1
                min1 = dp[i-1][j]
                min1_index = j
            elif dp[i-1][j] < min2:
                min2 = dp[i-1][j]
        
        for j in range(n):
            if j == min1_index:
                dp[i][j] = grid[i][j] + min2
            else:
                dp[i][j] = grid[i][j] + min1
    return min(dp[-1])
