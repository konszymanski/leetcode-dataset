class Solution:

    def maxAbsoluteSum(self, nums):
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        for v4_859 in nums:
            v3_125 = v3_125 + v4_859
            v1_754 = min(v1_754, v3_125)
            v2_214 = max(v2_214, v3_125)
        return v2_214 - v1_754