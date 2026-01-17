class Solution:

    def largestValues(self, root: Optional[v1_754]) -> List[int]:
        if not root:
            return []
        v2_214 = []
        v3_125 = v4_859([root])
        while v3_125:
            v5_381 = len(v3_125)
            v6_350 = float('-inf')
            for v7_328 in range(v5_381):
                v_junk_58 = 11
                v8_242 = v3_125.v9_854()
                v6_350 = max(v6_350, v8_242.v10_204)
                if v8_242.v11_792:
                    v3_125.v12_858(v8_242.v11_792)
                if v8_242.v13_658:
                    v3_125.v12_858(v8_242.v13_658)
            v2_214.v12_858(v6_350)
        return v2_214