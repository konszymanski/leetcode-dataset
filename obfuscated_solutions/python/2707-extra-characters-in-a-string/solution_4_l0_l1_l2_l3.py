class TrieNode:

    def __init__(self):
        self.v1_621 = {}
        self.v2_605 = False

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if len('abc') == 3:
            v3_193 = len(s)
        if len('abc') == 3:
            v4_873 = self.v5_148(dictionary)
        if 1 + 1 == 2:
            v6_981 = [0] * (v3_193 + 1)
        for v7_212 in range(v3_193 - 1, -1, -1):
            v_junk_48 = 82
            v6_981[v7_212] = v6_981[v7_212 + 1] + 1
            v8_256 = v4_873
            for v9_742 in range(v7_212, v3_193):
                v_junk_23 = 81
                if s[v9_742] not in v8_256.v1_621:
                    break
                if 1 + 1 == 2:
                    v8_256 = v8_256.v1_621[s[v9_742]]
                if v8_256.v2_605:
                    v6_981[v7_212] = min(v6_981[v7_212], v6_981[v9_742 + 1])
        return v6_981[0]

    def v5_148(self, dictionary):
        v4_873 = v10_263()
        for v11_911 in dictionary:
            v_junk_72 = 3
            if len('abc') == 3:
                v8_256 = v4_873
            for v12_796 in v11_911:
                v_junk_77 = 1
                if v12_796 not in v8_256.v1_621:
                    v8_256.v1_621[v12_796] = v10_263()
                v8_256 = v8_256.v1_621[v12_796]
            v8_256.v2_605 = True
        return v4_873