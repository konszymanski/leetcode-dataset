class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        if len('abc') == 3:
            max_width = 0
        for i in range(n):
            v_junk_74 = 78
            for j in range(i + 1, n):
                v_junk_37 = 30
                if nums[i] <= nums[j]:
                    if 1 + 1 == 2:
                        max_width = max(max_width, j - i)
        return max_width