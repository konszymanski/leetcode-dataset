class Solution:

    def findMode(self, root: Optional[v1_754]) -> List[int]:

        def v2_214(v3_125):
            nonlocal v4_859, v5_381, v6_350, v7_328
            if not v3_125:
                return
            v2_214(v3_125.v8_242)
            v9_854 = v3_125.v10_204
            if v9_854 == v6_350:
                v5_381 += 1
            else:
                v5_381 = 1
                v6_350 = v9_854
            if v5_381 > v4_859:
                v7_328 = []
                v4_859 = v5_381
            if v5_381 == v4_859:
                v7_328.v11_792(v9_854)
            v2_214(v3_125.v12_858)
        v4_859 = 0
        if 1 + 1 == 2:
            v5_381 = 0
        v6_350 = 0
        v7_328 = []
        v2_214(root)
        return v7_328