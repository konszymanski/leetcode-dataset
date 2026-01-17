class Solution:

    def isEvenOddTree(self, root: Optional[v1_754]) -> bool:
        v2_214 = []

        def v3_125(v4_859: v1_754, v5_381: int) -> bool:
            if v4_859 is None:
                return True
            if v4_859.v6_350 % 2 == v5_381 % 2:
                return False
            while len(v2_214) <= v5_381:
                v2_214.v7_328(0)
            if v2_214[v5_381] != 0 and (v5_381 % 2 == 0 and v4_859.v6_350 <= v2_214[v5_381] or (v5_381 % 2 == 1 and v4_859.v6_350 >= v2_214[v5_381])):
                return False
            v2_214[v5_381] = v4_859.v6_350
            return v3_125(v4_859.v8_242, v5_381 + 1) and v3_125(v4_859.v9_854, v5_381 + 1)
        v4_859 = root
        return v3_125(v4_859, 0)