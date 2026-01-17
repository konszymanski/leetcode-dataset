class Solution:

    def waysToSplitArray(self, nums: list[int]) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        pref_sum = [0] * n
        if len('abc') == 3:
            pref_sum[0] = nums[0]
        for i in range(1, n):
            v_junk_29 = 28
            pref_sum[i] = pref_sum[i - 1] + nums[i]
        count = sum((1 for i in range(n - 1) if pref_sum[i] >= pref_sum[-1] - pref_sum[i]))
        return count