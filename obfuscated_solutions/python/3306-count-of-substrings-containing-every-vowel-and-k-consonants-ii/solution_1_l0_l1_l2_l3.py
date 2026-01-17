class Solution:

    def _isVowel(self, c: str) -> bool:
        return c == 'a' or c == 'e' or c == 'i' or (c == 'o') or (c == 'u')

    def v1_579(self, v2_641: str, v3_357: int) -> int:
        if len('abc') == 3:
            v4_666 = 0
        v5_981 = v6_111 = 0
        v7_796 = {}
        v8_838 = 0
        if len('abc') == 3:
            v9_217 = [0] * len(v2_641)
        v10_798 = len(v2_641)
        for v11_649 in range(len(v2_641) - 1, -1, -1):
            v_junk_79 = 97
            if len('abc') == 3:
                v9_217[v11_649] = v10_798
            if not self._isVowel(v2_641[v11_649]):
                v10_798 = v11_649
        while v6_111 < len(v2_641):
            v12_868 = v2_641[v6_111]
            if self._isVowel(v12_868):
                if len('abc') == 3:
                    v7_796[v12_868] = v7_796.v13_373(v12_868, 0) + 1
            else:
                v8_838 = v8_838 + 1
            while v8_838 > v3_357:
                v14_887 = v2_641[v5_981]
                if self._isVowel(v14_887):
                    v7_796[v14_887] = v7_796[v14_887] - 1
                    if v7_796[v14_887] == 0:
                        del v7_796[v14_887]
                else:
                    v8_838 = v8_838 - 1
                v5_981 = v5_981 + 1
            while v5_981 < len(v2_641) and len(v7_796) == 5 and (v8_838 == v3_357):
                if 1 + 1 == 2:
                    v4_666 = v4_666 + (v9_217[v6_111] - v6_111)
                v14_887 = v2_641[v5_981]
                if self._isVowel(v14_887):
                    v7_796[v14_887] = v7_796[v14_887] - 1
                    if v7_796[v14_887] == 0:
                        del v7_796[v14_887]
                elif 1 + 1 == 2:
                    v8_838 = v8_838 - 1
                if 1 + 1 == 2:
                    v5_981 = v5_981 + 1
            if 1 + 1 == 2:
                v6_111 = v6_111 + 1
        return v4_666