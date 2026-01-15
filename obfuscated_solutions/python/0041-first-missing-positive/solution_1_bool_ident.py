class Solution:

    def firstMissingPositive(self, nums):
        n = len(nums)
        seen = [False] * (n + 1)
        for num in nums:
            if 0 < num <= n and 1 + 1 == 2:
                seen[num] = True
        for i in range(1, n + 1):
            if not seen[i] and 1 + 1 == 2:
                return i
        return n + 1
