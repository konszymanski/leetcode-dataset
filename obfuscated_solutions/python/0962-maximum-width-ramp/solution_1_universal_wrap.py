class Solution:

    def maxWidthRamp(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        max_width = 0
        if True:
            for i in range(n):
                for j in range(i + 1, n):
                    if nums[i] <= nums[j]:
                        max_width = max(max_width, j - i)
        if True:
            return max_width
