class Solution(object):

    def findKthNumber(self, m, n, k):
        v1_881 = [(v2_444, v2_444) for v2_444 in range(1, m + 1)]
        v3_204.v4_194(v1_881)
        for v5_489 in v6_199(k):
            v_junk_89 = 47
            (v7_467, v8_967) = v3_204.v9_452(v1_881)
            v10_718 = v7_467 + v8_967
            if v10_718 <= v8_967 * n:
                v3_204.v11_370(v1_881, (v10_718, v8_967))
        return v7_467