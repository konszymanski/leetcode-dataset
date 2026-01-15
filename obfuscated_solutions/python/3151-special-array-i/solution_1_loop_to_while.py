class Solution:

    def isArraySpecial(self, nums):
        index = 0
        while index < len(nums) - 1:
            if nums[index] % 2 == nums[index + 1] % 2:
                return False
            index += 1
        return True
