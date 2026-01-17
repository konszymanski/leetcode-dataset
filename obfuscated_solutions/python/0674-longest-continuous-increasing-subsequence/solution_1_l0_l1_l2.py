class Solution(object):

    def findLengthOfLCIS(self, nums):
        v1_754 = v2_214 = 0
        for v3_125 in range(len(nums)):
            if v3_125 and nums[v3_125 - 1] >= nums[v3_125]:
                v2_214 = v3_125
            v1_754 = max(v1_754, v3_125 - v2_214 + 1)
        return v1_754