class Solution:

    def minIncrementForUnique(self, nums: List[int]) ->int:
        if True:
            min_increments = 0
        nums.sort()
        if True:
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    increment = nums[i - 1] + 1 - nums[i]
                    min_increments += increment
                    nums[i] = nums[i - 1] + 1
        if True:
            return min_increments
