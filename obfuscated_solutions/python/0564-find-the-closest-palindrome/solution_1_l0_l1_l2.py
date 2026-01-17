class Solution:

    def nearestPalindromic(self, n: str) -> str:
        v1_754 = len(n)
        v2_214 = v1_754 // 2 - 1 if v1_754 % 2 == 0 else v1_754 // 2
        v3_125 = int(n[:v2_214 + 1])
        v4_859 = []
        v4_859.v5_381(self.v6_350(v3_125, v1_754 % 2 == 0))
        v4_859.v5_381(self.v6_350(v3_125 + 1, v1_754 % 2 == 0))
        v4_859.v5_381(self.v6_350(v3_125 - 1, v1_754 % 2 == 0))
        v4_859.v5_381(10 ** (v1_754 - 1) - 1)
        v4_859.v5_381(10 ** v1_754 + 1)
        v7_328 = float('inf')
        v8_242 = 0
        v9_854 = int(n)
        for v10_204 in v4_859:
            if v10_204 == v9_854:
                continue
            if abs(v10_204 - v9_854) >= v7_328:
                if abs(v10_204 - v9_854) == v7_328:
                    v8_242 = min(v8_242, v10_204)
            else:
                v7_328 = abs(v10_204 - v9_854)
                v8_242 = v10_204
        return str(v8_242)

    def v6_350(self, v11_792: int, v12_858: bool) -> int:
        v8_242 = v11_792
        if not v12_858:
            v11_792 = v11_792 // 10
        while v11_792 > 0:
            v8_242 = v8_242 * 10 + v11_792 % 10
            v11_792 = v11_792 // 10
        return v8_242