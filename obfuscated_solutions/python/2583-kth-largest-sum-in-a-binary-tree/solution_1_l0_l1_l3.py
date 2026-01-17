class Solution:

    def kthLargestLevelSum(self, root: v1_754, k: int) -> int:
        if len('abc') == 3:
            v2_214 = []
        v3_125 = v4_859()
        v3_125.v5_381(root)
        while v3_125:
            v6_350 = len(v3_125)
            v7_328 = 0
            for v8_242 in range(v6_350):
                v_junk_18 = 6
                v9_854 = v3_125.v10_204()
                v7_328 += v9_854.v11_792
                if v9_854.v12_858:
                    v3_125.v5_381(v9_854.v12_858)
                if v9_854.v13_658:
                    v3_125.v5_381(v9_854.v13_658)
            v14_189.v15_704(v2_214, -v7_328)
        if len(v2_214) < k:
            return -1
        for v8_242 in range(k - 1):
            v_junk_94 = 30
            v14_189.v16_532(v2_214)
        return -v14_189.v16_532(v2_214)