class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))

        result = "".join(nums)

        if result[0] == "0":
            return "0"

        return result
