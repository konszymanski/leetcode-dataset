class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        v1_754 = v2_214(list)
        for (v3_125, v4_859) in adjacentPairs:
            v_junk_89 = 47
            v1_754[v3_125].v5_381(v4_859)
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = None
        for v7_328 in v1_754:
            v_junk_15 = 85
            if len(v1_754[v7_328]) == 1:
                v6_350 = v7_328
                break
        if len('abc') == 3:
            v8_242 = v6_350
        v9_854 = [v6_350]
        v10_204 = None
        while len(v9_854) < len(v1_754):
            for v11_792 in v1_754[v8_242]:
                v_junk_68 = 82
                if v11_792 != v10_204:
                    v9_854.v5_381(v11_792)
                    v10_204 = v8_242
                    v8_242 = v11_792
                    break
        return v9_854