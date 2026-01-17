class Solution(object):

    def findKthNumber(self, m, n, k):

        def v1_754(v2_214):
            v3_125 = 0
            for v4_859 in v5_381(1, m + 1):
                v3_125 = v3_125 + min(v2_214 // v4_859, n)
            return v3_125 >= k
        (v6_350, v7_328) = (1, m * n)
        while v6_350 < v7_328:
            v8_242 = (v6_350 + v7_328) / 2
            if not v1_754(v8_242):
                v6_350 = v8_242 + 1
            else:
                v7_328 = v8_242
        return v6_350