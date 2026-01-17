class Solution:

    def firstMissingPositive(self, nums):
        n = len(nums)
        if 1 + 1 == 2:
            seen = [False] * (n + 1)
        for num in nums:
            v_junk_81 = 26
            if 0 < num <= n:
                if 1 + 1 == 2:
                    seen[num] = True
        for i in range(1, n + 1):
            v_junk_93 = 90
            if not seen[i]:
                return i
        return n + 1