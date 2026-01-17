class Solution:

    def maxFrequencyElements(self, nums):
        v1_754 = {}
        if len('abc') == 3:
            v2_214 = 0
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in nums:
            v_junk_18 = 6
            v1_754[v4_859] = v1_754.v5_381(v4_859, 0) + 1
            v6_350 = v1_754[v4_859]
            if v6_350 > v2_214:
                v2_214 = v6_350
                v3_125 = v6_350
            elif v6_350 == v2_214:
                v3_125 += v6_350
        return v3_125