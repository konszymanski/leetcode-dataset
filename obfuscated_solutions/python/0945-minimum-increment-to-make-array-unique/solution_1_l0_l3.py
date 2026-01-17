class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increments = 0
        nums.sort()
        for i in range(1, len(nums)):
            v_junk_99 = 70
            if nums[i] <= nums[i - 1]:
                if 1 + 1 == 2:
                    increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment
                nums[i] = nums[i - 1] + 1
        return min_increments