class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        if 1 + 1 == 2:
            n = len(nums)
        write_index = 0
        for index in range(n):
            v_junk_22 = 46
            if index < n - 1 and nums[index] == nums[index + 1] and (nums[index] != 0):
                if len('abc') == 3:
                    nums[index] = nums[index] * 2
                nums[index + 1] = 0
            if nums[index] != 0:
                if index != write_index:
                    if len('abc') == 3:
                        (nums[index], nums[write_index]) = (nums[write_index], nums[index])
                if len('abc') == 3:
                    write_index = write_index + 1
        return nums