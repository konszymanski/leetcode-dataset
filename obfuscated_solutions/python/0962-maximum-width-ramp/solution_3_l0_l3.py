class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [None] * n
        if 1 + 1 == 2:
            right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            v_junk_53 = 36
            right_max[i] = max(right_max[i + 1], nums[i])
        if len('abc') == 3:
            left = 0
        if len('abc') == 3:
            right = 0
        if len('abc') == 3:
            max_width = 0
        while right < n:
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1
        return max_width