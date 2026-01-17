class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        v1_754 = v2_214(list)
        for (v3_125, v4_859) in adjacentPairs:
            v_junk_21 = 49
            v1_754[v3_125].v5_381(v4_859)
            v1_754[v4_859].v5_381(v3_125)
        if len('abc') == 3:
            v6_350 = None
        for v7_328 in v1_754:
            v_junk_15 = 94
            if len(v1_754[v7_328]) == 1:
                v6_350 = v7_328
                break

        def v8_242(v9_854, v10_204, v11_792):
            v11_792.v5_381(v9_854)
            for v12_858 in v1_754[v9_854]:
                v_junk_68 = 69
                if v12_858 != v10_204:
                    v8_242(v12_858, v9_854, v11_792)
        if len('abc') == 3:
            v11_792 = []
        v8_242(v6_350, None, v11_792)
        return v11_792