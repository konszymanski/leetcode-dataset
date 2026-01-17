class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.v1_754 = 0
        self.v2_214 = 0

    def v3_125(self, v4_859: List[int], v5_381: List[int]) -> Optional[v6_350]:
        return self.v7_328(v4_859, v5_381)

    def v7_328(self, v4_859: List[int], v5_381: List[int]) -> Optional[v6_350]:
        v8_242 = v6_350(v4_859[self.v1_754])
        self.v1_754 += 1
        if v8_242.v9_854 != v5_381[self.v2_214]:
            v8_242.v10_204 = self.v7_328(v4_859, v5_381)
        if v8_242.v9_854 != v5_381[self.v2_214]:
            v8_242.v11_792 = self.v7_328(v4_859, v5_381)
        self.v2_214 += 1
        return v8_242