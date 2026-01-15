class Solution:

    def minDifference(self, nums: List[int]) ->int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0
        nums.sort()
        min_diff = float('inf')
        left = 0
        while left < 4:
            right = nums_size - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])
            left += 1
        return min_diff
