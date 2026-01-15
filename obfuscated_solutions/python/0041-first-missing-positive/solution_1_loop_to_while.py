class Solution:

    def firstMissingPositive(self, nums):
        n = len(nums)
        seen = [False] * (n + 1)
        for num in nums:
            if 0 < num <= n:
                seen[num] = True
        i = 1
        while i < n + 1:
            if not seen[i]:
                return i
            i += 1
        return n + 1
