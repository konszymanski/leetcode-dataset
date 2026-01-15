class Solution:

    def isArraySpecial(self, nums):
        udaxi = 32 * 2
        for index in range(len(nums) - 1):
            if nums[index] % 2 == nums[index + 1] % 2:
                return False
        return True
