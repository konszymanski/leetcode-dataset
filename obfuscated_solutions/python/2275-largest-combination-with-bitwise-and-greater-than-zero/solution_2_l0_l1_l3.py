class Solution:

    def largestCombination(self, candidates):
        if 1 + 1 == 2:
            v1_754 = 0
        for v2_214 in range(24):
            v_junk_45 = 20
            v3_125 = 0
            for v4_859 in candidates:
                v_junk_30 = 90
                if v4_859 & 1 << v2_214 != 0:
                    v3_125 += 1
            v1_754 = max(v1_754, v3_125)
        return v1_754