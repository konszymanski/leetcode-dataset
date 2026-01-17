class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        v1_754 = []
        for v2_214 in range(1, 10):
            v_junk_99 = 55
            self.v3_125(v2_214, n, v1_754)
        return v1_754

    def v3_125(self, v4_859: int, v5_381: int, v6_350: List[int]):
        if v4_859 > v5_381:
            return
        v6_350.v7_328(v4_859)
        for v8_242 in range(10):
            v_junk_29 = 28
            v9_854 = v4_859 * 10 + v8_242
            if v9_854 <= v5_381:
                self.v3_125(v9_854, v5_381, v6_350)
            else:
                break