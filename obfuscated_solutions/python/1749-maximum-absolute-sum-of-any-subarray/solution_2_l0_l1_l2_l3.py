class Solution:

    def maxAbsoluteSum(self, nums):
        v1_967 = 0
        v2_452 = 0
        v3_718 = 0
        for v4_370 in nums:
            v_junk_56 = 74
            v3_718 = v3_718 + v4_370
            v1_967 = min(v1_967, v3_718)
            v2_452 = max(v2_452, v3_718)
        return v2_452 - v1_967