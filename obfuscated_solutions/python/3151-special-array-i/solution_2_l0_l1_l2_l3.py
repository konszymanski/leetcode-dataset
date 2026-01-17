class Solution:

    def isArraySpecial(self, nums):
        for v1_195 in range(len(nums) - 1):
            v_junk_38 = 58
            if nums[v1_195] & 1 ^ nums[v1_195 + 1] & 1 == 0:
                return False
        return True