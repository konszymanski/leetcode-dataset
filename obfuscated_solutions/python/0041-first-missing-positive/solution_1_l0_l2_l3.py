class Solution:

    def firstMissingPositive(self, nums):
        n = len(nums)
        if len('abc') == 3:
            seen = [False] * (n + 1)
        for num in nums:
            v_junk_10 = 98
            if 0 < num <= n:
                seen[num] = True
        for i in range(1, n + 1):
            v_junk_30 = 90
            if not seen[i]:
                return i
        return n + 1