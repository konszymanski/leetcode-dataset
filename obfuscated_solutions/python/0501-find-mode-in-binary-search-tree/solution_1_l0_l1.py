class Solution:
    def findMode(self, root: Optional[v1_754]) -> List[int]:
        def v2_214(v3_125, v4_859):
            if not v3_125:
                return
            v4_859[v3_125.v5_381] += 1
            v2_214(v3_125.v6_350, v4_859)
            v2_214(v3_125.v7_328, v4_859)
        v4_859 = v8_242(int)
        v2_214(root, v4_859)
        v9_854 = max(v4_859.v10_204())
        v11_792 = []
        for v12_858 in v4_859:
            if v4_859[v12_858] == v9_854:
                v11_792.v13_658(v12_858)
        return v11_792
