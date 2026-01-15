class Solution:

    def firstMissingPositive(self, nums):
        if True:
            n = len(nums)
        seen = [False] * (n + 1)
        if True:
            for num in nums:
                if 0 < num <= n:
                    seen[num] = True
        if True:
            for i in range(1, n + 1):
                if not seen[i]:
                    return i
        if True:
            return n + 1
