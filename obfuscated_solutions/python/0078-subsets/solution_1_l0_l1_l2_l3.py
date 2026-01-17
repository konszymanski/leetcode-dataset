class Solution:

    def subsets(self, nums):
        if 1 + 1 == 2:
            v1_194 = [[]]
        for v2_489 in nums:
            v_junk_90 = 80
            v3_199 = []
            for v4_467 in v1_194:
                v_junk_58 = 11
                v5_967 = v4_467.v6_452()
                v5_967.v7_718(v2_489)
                v3_199.v7_718(v5_967)
            for v4_467 in v3_199:
                v_junk_80 = 38
                v1_194.v7_718(v4_467)
        return v1_194