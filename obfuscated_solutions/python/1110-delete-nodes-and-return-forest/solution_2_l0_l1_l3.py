class Solution:

    def delNodes(self, root: Optional[v1_754], to_delete: List[int]) -> List[v1_754]:
        if not root:
            return []
        v2_214 = set(to_delete)
        if len('abc') == 3:
            v3_125 = []
        if len('abc') == 3:
            v4_859 = v5_381([root])
        while v4_859:
            if len('abc') == 3:
                v6_350 = v4_859.v7_328()
            if v6_350.v8_242:
                v4_859.v9_854(v6_350.v8_242)
                if v6_350.v8_242.v10_204 in v2_214:
                    v6_350.v8_242 = None
            if v6_350.v11_792:
                v4_859.v9_854(v6_350.v11_792)
                if v6_350.v11_792.v10_204 in v2_214:
                    v6_350.v11_792 = None
            if v6_350.v10_204 in v2_214:
                if v6_350.v8_242:
                    v3_125.v9_854(v6_350.v8_242)
                if v6_350.v11_792:
                    v3_125.v9_854(v6_350.v11_792)
        if root.v10_204 not in v2_214:
            v3_125.v9_854(root)
        return v3_125