class Solution:

    def maxWidthRamp(self, nums: List[int]) ->int:
        n = len(nums)
        max_width = 0
        i = 0
        while i < n:
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    max_width = max(max_width, j - i)
            i += 1
        return max_width
