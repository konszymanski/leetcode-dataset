class Solution:
    def isArraySpecial(self, nums):
        for v1_754 in range(len(nums)  -  1):
            if ((nums[v1_754] & 1) ^ (nums[v1_754 + 1]  &  1)) == 0:
                return False
        return True
