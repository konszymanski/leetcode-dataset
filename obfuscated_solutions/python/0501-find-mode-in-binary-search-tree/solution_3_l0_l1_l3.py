class Solution:

    def findMode(self, root: Optional[v1_754]) -> List[int]:
        v2_214 = v3_125(int)
        v4_859 = v5_381([root])
        while v4_859:
            v6_350 = v4_859.v7_328()
            v2_214[v6_350.v8_242] += 1
            if v6_350.v9_854:
                v4_859.v10_204(v6_350.v9_854)
            if v6_350.v11_792:
                v4_859.v10_204(v6_350.v11_792)
        v12_858 = max(v2_214.v13_658())
        v14_189 = []
        for v15_704 in v2_214:
            v_junk_58 = 11
            if v2_214[v15_704] == v12_858:
                v14_189.v10_204(v15_704)
        return v14_189