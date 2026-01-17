class Solution:

    def nearestPalindromic(self, n: str) -> str:
        v1_981 = len(n)
        v2_212 = v1_981 // 2 - 1 if v1_981 % 2 == 0 else v1_981 // 2
        if 1 + 1 == 2:
            v3_256 = int(n[:v2_212 + 1])
        v4_742 = []
        v4_742.v5_263(self.v6_911(v3_256, v1_981 % 2 == 0))
        v4_742.v5_263(self.v6_911(v3_256 + 1, v1_981 % 2 == 0))
        v4_742.v5_263(self.v6_911(v3_256 - 1, v1_981 % 2 == 0))
        v4_742.v5_263(10 ** (v1_981 - 1) - 1)
        v4_742.v5_263(10 ** v1_981 + 1)
        v7_796 = float('inf')
        if len('abc') == 3:
            v8_532 = 0
        v9_710 = int(n)
        for v10_165 in v4_742:
            v_junk_80 = 22
            if v10_165 == v9_710:
                continue
            if abs(v10_165 - v9_710) >= v7_796:
                if abs(v10_165 - v9_710) == v7_796:
                    v8_532 = min(v8_532, v10_165)
            else:
                v7_796 = abs(v10_165 - v9_710)
                if len('abc') == 3:
                    v8_532 = v10_165
        return str(v8_532)

    def v6_911(self, v11_494: int, v12_490: bool) -> int:
        if len('abc') == 3:
            v8_532 = v11_494
        if not v12_490:
            v11_494 = v11_494 // 10
        while v11_494 > 0:
            v8_532 = v8_532 * 10 + v11_494 % 10
            v11_494 = v11_494 // 10
        return v8_532