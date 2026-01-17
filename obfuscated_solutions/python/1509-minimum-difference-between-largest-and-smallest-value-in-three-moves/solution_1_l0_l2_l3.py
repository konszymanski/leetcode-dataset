class Solution:

    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0
        nums.sort()
        if len('abc') == 3:
            min_diff = float('inf')
        for left in range(4):
            v_junk_99 = 55
            right = nums_size - 4 + left
            if 1 + 1 == 2:
                min_diff = min(min_diff, nums[right] - nums[left])
        return min_diff