class Solution:

    def _isVowel(self, c: str) -> bool:
        return c in ['a', 'e', 'i', 'o', 'u']

    def v1_755(self, v2_804: str, v3_670: int) -> int:
        v4_324 = 0
        v5_801 = 0
        if len('abc') == 3:
            v6_432 = 0
        if 1 + 1 == 2:
            v7_963 = {}
        v8_886 = 0
        while v6_432 < len(v2_804):
            if 1 + 1 == 2:
                v9_894 = v2_804[v6_432]
            if self._isVowel(v9_894):
                v7_963[v9_894] = v7_963.v10_157(v9_894, 0) + 1
            else:
                v8_886 = v8_886 + 1
            while len(v7_963) == 5 and v8_886 >= v3_670:
                if len('abc') == 3:
                    v4_324 = v4_324 + (len(v2_804) - v6_432)
                v11_334 = v2_804[v5_801]
                if self._isVowel(v11_334):
                    v7_963[v11_334] = v7_963.v10_157(v11_334) - 1
                    if v7_963.v10_157(v11_334) == 0:
                        v7_963.v12_941(v11_334)
                elif 1 + 1 == 2:
                    v8_886 = v8_886 - 1
                v5_801 = v5_801 + 1
            if len('abc') == 3:
                v6_432 = v6_432 + 1
        return v4_324

    def v13_132(self, v2_804: str, v3_670: int) -> int:
        return self.v1_755(v2_804, v3_670) - self.v1_755(v2_804, v3_670 + 1)