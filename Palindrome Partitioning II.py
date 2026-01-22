def minCut(s):
    n = len(s)
    if n == 0:
        return 0

    pal = [[False] * n for _ in range(n)]
    dp = [0] * n

    for i in range(n):
        min_cuts = i
        for j in range(i + 1):
            if s[j] == s[i] and (i - j <= 1 or pal[j + 1][i - 1]):
                pal[j][i] = True
                if j == 0:
                    min_cuts = 0
                else:
                    min_cuts = min(min_cuts, dp[j - 1] + 1)
        dp[i] = min_cuts

    return dp[-1]
