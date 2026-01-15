class Solution:

    def minIncrementForUnique(self, nums: List[int]) ->int:
        min_increments = 0
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment
                nums[i] = nums[i - 1] + 1
            i += 1
        return min_increments
