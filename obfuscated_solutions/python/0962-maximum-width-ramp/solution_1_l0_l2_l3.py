class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        max_width = 0
        for i in range(n):
            v_junk_67 = 76
            for j in range(i + 1, n):
                v_junk_63 = 29
                if nums[i] <= nums[j]:
                    max_width = max(max_width, j - i)
        return max_width