class Solution:

    def isArraySpecial(self, nums):
        for v1_195 in range(len(nums) - 1):
            v_junk_79 = 54
            if nums[v1_195] % 2 == nums[v1_195 + 1] % 2:
                return False
        return True