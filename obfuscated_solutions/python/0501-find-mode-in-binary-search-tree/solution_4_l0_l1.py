class Solution:
    def findMode(self, root: Optional[v1_754]) -> List[int]:
        def v2_214(v3_125, v4_859):
            if not v3_125:
                return
            v2_214(v3_125.v5_381, v4_859)
            v4_859.v6_350(v3_125.v7_328)
            v2_214(v3_125.v8_242, v4_859)
        v4_859 = []
        v2_214(root, v4_859)
        v9_854 = 0
        v10_204 = 0
        v11_792 = 0
        v12_858 = []
        for v13_658 in v4_859:
            if v13_658 == v11_792:
                v10_204 += 1
            else:
                v10_204 = 1
                v11_792 = v13_658
            if v10_204  >  v9_854:
                v12_858 = []
                v9_854 = v10_204
            if v10_204 == v9_854:
                v12_858.v6_350(v13_658)
        return v12_858
