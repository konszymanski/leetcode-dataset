class Solution:

    def largestCombination(self, candidates):
        v1_754 = 0
        for v2_214 in range(24):
            v3_125 = 0
            for v4_859 in candidates:
                if v4_859 & 1 << v2_214 != 0:
                    v3_125 = v3_125 + 1
            v1_754 = max(v1_754, v3_125)
        return v1_754