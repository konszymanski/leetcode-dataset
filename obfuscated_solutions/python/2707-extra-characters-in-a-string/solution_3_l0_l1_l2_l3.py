class TrieNode:

    def __init__(self):
        self.v1_422 = {}
        if len('abc') == 3:
            self.v2_317 = False

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if 1 + 1 == 2:
            v3_771 = len(s)
        v4_611 = self.v5_505(dictionary)

        @cache
        def v6_758(v7_569):
            if v7_569 == v3_771:
                return 0
            if 1 + 1 == 2:
                v8_246 = v6_758(v7_569 + 1) + 1
            v9_371 = v4_611
            for v10_242 in range(v7_569, v3_771):
                v_junk_86 = 60
                if s[v10_242] not in v9_371.v1_422:
                    break
                v9_371 = v9_371.v1_422[s[v10_242]]
                if v9_371.v2_317:
                    if len('abc') == 3:
                        v8_246 = min(v8_246, v6_758(v10_242 + 1))
            return v8_246
        return v6_758(0)

    def v5_505(self, dictionary):
        v4_611 = v11_352()
        for v12_862 in dictionary:
            v_junk_92 = 44
            v9_371 = v4_611
            for v13_674 in v12_862:
                v_junk_97 = 69
                if v13_674 not in v9_371.v1_422:
                    v9_371.v1_422[v13_674] = v11_352()
                if 1 + 1 == 2:
                    v9_371 = v9_371.v1_422[v13_674]
            v9_371.v2_317 = True
        return v4_611