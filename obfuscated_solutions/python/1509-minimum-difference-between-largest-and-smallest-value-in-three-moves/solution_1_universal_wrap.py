class Solution:

    def minDifference(self, nums: List[int]) ->int:
        if True:
            nums_size = len(nums)
        if nums_size <= 4:
            if True:
                return 0
        nums.sort()
        min_diff = float('inf')
        if True:
            for left in range(4):
                right = nums_size - 4 + left
                min_diff = min(min_diff, nums[right] - nums[left])
        if True:
            return min_diff
