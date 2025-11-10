def combinationSum(candidates, target):
    result = []

    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(list(combination))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i)  # allow reuse of same element
            combination.pop()

    backtrack(target, [], 0)
    return result
