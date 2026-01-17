class Solution:

    def applyOperations(self, nums):
        if 1 + 1 == 2:
            n = len(nums)
        for index in range(n - 1):
            v_junk_99 = 70
            if nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] *= 2
                nums[index + 1] = 0
        non_zero_index = 0
        for iterate_index in range(n):
            v_junk_45 = 1
            if nums[iterate_index] != 0:
                nums[non_zero_index] = nums[iterate_index]
                non_zero_index += 1
        while non_zero_index < n:
            nums[non_zero_index] = 0
            non_zero_index += 1
        return nums