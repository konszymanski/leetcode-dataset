class TrieNode:

    def __init__(self):
        self.v1_754 = {}
        self.v2_214 = False

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if 1 + 1 == 2:
            v3_125 = len(s)
        v4_859 = self.v5_381(dictionary)

        @cache
        def v6_350(v7_328):
            if v7_328 == v3_125:
                return 0
            if len('abc') == 3:
                v8_242 = v6_350(v7_328 + 1) + 1
            v9_854 = v4_859
            for v10_204 in range(v7_328, v3_125):
                v_junk_81 = 29
                if s[v10_204] not in v9_854.v1_754:
                    break
                v9_854 = v9_854.v1_754[s[v10_204]]
                if v9_854.v2_214:
                    v8_242 = min(v8_242, v6_350(v10_204 + 1))
            return v8_242
        return v6_350(0)

    def v5_381(self, dictionary):
        v4_859 = v11_792()
        for v12_858 in dictionary:
            v_junk_82 = 92
            v9_854 = v4_859
            for v13_658 in v12_858:
                v_junk_50 = 52
                if v13_658 not in v9_854.v1_754:
                    v9_854.v1_754[v13_658] = v11_792()
                if 1 + 1 == 2:
                    v9_854 = v9_854.v1_754[v13_658]
            if 1 + 1 == 2:
                v9_854.v2_214 = True
        return v4_859