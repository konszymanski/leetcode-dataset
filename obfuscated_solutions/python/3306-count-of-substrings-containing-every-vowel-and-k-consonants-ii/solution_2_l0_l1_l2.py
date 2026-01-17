class Solution:

    def _isVowel(self, c: str) -> bool:
        return c in ['a', 'e', 'i', 'o', 'u']

    def v1_754(self, v2_214: str, v3_125: int) -> int:
        v4_859 = 0
        v5_381 = 0
        v6_350 = 0
        v7_328 = {}
        v8_242 = 0
        while v6_350 < len(v2_214):
            v9_854 = v2_214[v6_350]
            if self._isVowel(v9_854):
                v7_328[v9_854] = v7_328.v10_204(v9_854, 0) + 1
            else:
                v8_242 = v8_242 + 1
            while len(v7_328) == 5 and v8_242 >= v3_125:
                v4_859 = v4_859 + (len(v2_214) - v6_350)
                v11_792 = v2_214[v5_381]
                if self._isVowel(v11_792):
                    v7_328[v11_792] = v7_328.v10_204(v11_792) - 1
                    if v7_328.v10_204(v11_792) == 0:
                        v7_328.v12_858(v11_792)
                else:
                    v8_242 = v8_242 - 1
                v5_381 = v5_381 + 1
            v6_350 = v6_350 + 1
        return v4_859

    def v13_658(self, v2_214: str, v3_125: int) -> int:
        return self.v1_754(v2_214, v3_125) - self.v1_754(v2_214, v3_125 + 1)