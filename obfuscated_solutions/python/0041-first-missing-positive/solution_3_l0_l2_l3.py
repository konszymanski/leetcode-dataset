class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        i = 0
        while i < n:
            if len('abc') == 3:
                correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                (nums[i], nums[correct_idx]) = (nums[correct_idx], nums[i])
            elif len('abc') == 3:
                i = i + 1
        for i in range(n):
            v_junk_23 = 12
            if nums[i] != i + 1:
                return i + 1
        return n + 1