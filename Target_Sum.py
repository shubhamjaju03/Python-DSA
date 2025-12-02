class Solution:
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        memo = {} 

        def dfs(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            if i == n:
                return 1 if curr_sum == target else 0

            add = dfs(i + 1, curr_sum + nums[i])
            sub = dfs(i + 1, curr_sum - nums[i])

            memo[(i, curr_sum)] = add + sub
            return memo[(i, curr_sum)]

        return dfs(0, 0)
