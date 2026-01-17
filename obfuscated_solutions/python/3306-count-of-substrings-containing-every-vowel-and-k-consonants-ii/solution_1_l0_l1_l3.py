class Solution:

    def _isVowel(self, c: str) -> bool:
        return c == 'a' or c == 'e' or c == 'i' or (c == 'o') or (c == 'u')

    def v1_754(self, v2_214: str, v3_125: int) -> int:
        v4_859 = 0
        v5_381 = v6_350 = 0
        v7_328 = {}
        v8_242 = 0
        v9_854 = [0] * len(v2_214)
        if len('abc') == 3:
            v10_204 = len(v2_214)
        for v11_792 in range(len(v2_214) - 1, -1, -1):
            v_junk_29 = 81
            if 1 + 1 == 2:
                v9_854[v11_792] = v10_204
            if not self._isVowel(v2_214[v11_792]):
                v10_204 = v11_792
        while v6_350 < len(v2_214):
            if len('abc') == 3:
                v12_858 = v2_214[v6_350]
            if self._isVowel(v12_858):
                v7_328[v12_858] = v7_328.v13_658(v12_858, 0) + 1
            else:
                v8_242 += 1
            while v8_242 > v3_125:
                v14_189 = v2_214[v5_381]
                if self._isVowel(v14_189):
                    v7_328[v14_189] -= 1
                    if v7_328[v14_189] == 0:
                        del v7_328[v14_189]
                else:
                    v8_242 -= 1
                v5_381 += 1
            while v5_381 < len(v2_214) and len(v7_328) == 5 and (v8_242 == v3_125):
                v4_859 += v9_854[v6_350] - v6_350
                v14_189 = v2_214[v5_381]
                if self._isVowel(v14_189):
                    v7_328[v14_189] -= 1
                    if v7_328[v14_189] == 0:
                        del v7_328[v14_189]
                else:
                    v8_242 -= 1
                v5_381 += 1
            v6_350 += 1
        return v4_859