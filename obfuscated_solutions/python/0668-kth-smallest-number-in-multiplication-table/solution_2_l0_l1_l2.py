class Solution(object):

    def findKthNumber(self, m, n, k):
        v1_754 = [(v2_214, v2_214) for v2_214 in range(1, m + 1)]
        v3_125.v4_859(v1_754)
        for v5_381 in v6_350(k):
            (v7_328, v8_242) = v3_125.v9_854(v1_754)
            v10_204 = v7_328 + v8_242
            if v10_204 <= v8_242 * n:
                v3_125.v11_792(v1_754, (v10_204, v8_242))
        return v7_328