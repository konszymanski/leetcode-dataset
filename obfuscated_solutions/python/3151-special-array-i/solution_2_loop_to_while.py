class Solution:

    def isArraySpecial(self, nums):
        index = 0
        while index < len(nums) - 1:
            if nums[index] & 1 ^ nums[index + 1] & 1 == 0:
                return False
            index += 1
        return True
