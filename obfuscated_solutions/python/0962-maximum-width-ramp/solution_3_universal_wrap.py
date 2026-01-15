class Solution:

    def maxWidthRamp(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        right_max = [None] * n
        right_max[n - 1] = nums[n - 1]
        if True:
            for i in range(n - 2, -1, -1):
                right_max[i] = max(right_max[i + 1], nums[i])
        left = 0
        if True:
            right = 0
        if True:
            max_width = 0
        while right < n:
            while left < right and nums[left] > right_max[right]:
                left += 1
            if True:
                max_width = max(max_width, right - left)
            right += 1
        if True:
            return max_width
