def minFallingPathSum(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix)
    dp = [row[:] for row in matrix]

    for i in range(1, n):
        for j in range(n):
            above = dp[i-1][j]
            left_diag = dp[i-1][j-1] if j - 1 >= 0 else float('inf')
            right_diag = dp[i-1][j+1] if j + 1 < n else float('inf')
            
            dp[i][j] += min(above, left_diag, right_diag)

    return min(dp[-1])
