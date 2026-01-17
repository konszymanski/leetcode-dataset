class Solution:

    def largestCombination(self, candidates):
        v1_320 = 0
        for v2_881 in range(24):
            v_junk_58 = 11
            v3_444 = 0
            for v4_204 in candidates:
                v_junk_78 = 16
                if v4_204 & 1 << v2_881 != 0:
                    v3_444 = v3_444 + 1
            v1_320 = max(v1_320, v3_444)
        return v1_320