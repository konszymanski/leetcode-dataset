class Solution:

    def applyOperations(self, nums):
        if len('abc') == 3:
            n = len(nums)
        for index in range(n - 1):
            v_junk_23 = 12
            if nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] = nums[index] * 2
                if len('abc') == 3:
                    nums[index + 1] = 0
        non_zero_index = 0
        for iterate_index in range(n):
            v_junk_43 = 6
            if nums[iterate_index] != 0:
                nums[non_zero_index] = nums[iterate_index]
                non_zero_index = non_zero_index + 1
        while non_zero_index < n:
            nums[non_zero_index] = 0
            non_zero_index = non_zero_index + 1
        return nums