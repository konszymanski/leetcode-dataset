class Solution:

    def largestValues(self, root: Optional[v1_754]) -> List[int]:
        if not root:
            return []
        v2_214 = []
        v3_125 = [(root, 0)]
        while v3_125:
            (v4_859, v5_381) = v3_125.v6_350()
            if v5_381 != len(v2_214):
                v2_214[v5_381] = max(v2_214[v5_381], v4_859.v8_242)
            else:
                v2_214.v7_328(v4_859.v8_242)
            if v4_859.v9_854:
                v3_125.v7_328((v4_859.v9_854, v5_381 + 1))
            if v4_859.v10_204:
                v3_125.v7_328((v4_859.v10_204, v5_381 + 1))
        return v2_214