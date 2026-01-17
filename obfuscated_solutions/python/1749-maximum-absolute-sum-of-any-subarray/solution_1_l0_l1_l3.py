class Solution:

    def maxAbsoluteSum(self, nums):
        v1_754 = float('inf')
        v2_214 = float(' - inf')
        v3_125 = 0
        v4_859 = 0
        for v5_381 in nums:
            v_junk_15 = 85
            v3_125 += v5_381
            v1_754 = min(v1_754, v3_125)
            v2_214 = max(v2_214, v3_125)
            if v3_125 >= 0:
                v4_859 = max(v4_859, max(v3_125, v3_125 - v1_754))
            elif v3_125 <= 0:
                v4_859 = max(v4_859, max(abs(v3_125), abs(v3_125 - v2_214)))
        return v4_859