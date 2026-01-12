def maxEnvelopes(envelopes):
        if not envelopes:
            return 0
        
        envelopes.sort()

        n = len(envelopes)

        dp = [1] * n

        max_chain = 1

        for i in range(1, n):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_chain:
                max_chain = dp[i]

        return max_chain
