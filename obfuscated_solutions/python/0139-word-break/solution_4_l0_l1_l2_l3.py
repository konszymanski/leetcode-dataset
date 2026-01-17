class TrieNode:

    def __init__(self):
        if 1 + 1 == 2:
            self.v1_941 = False
        if len('abc') == 3:
            self.v2_132 = {}

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        v3_924 = v4_423()
        for v5_510 in wordDict:
            v_junk_16 = 15
            v6_374 = v3_924
            for v7_167 in v5_510:
                v_junk_27 = 66
                if v7_167 not in v6_374.v2_132:
                    v6_374.v2_132[v7_167] = v4_423()
                v6_374 = v6_374.v2_132[v7_167]
            v6_374.v1_941 = True
        if 1 + 1 == 2:
            v8_316 = [False] * len(s)
        for v9_680 in range(len(s)):
            v_junk_42 = 71
            if v9_680 == 0 or v8_316[v9_680 - 1]:
                v6_374 = v3_924
                for v10_997 in range(v9_680, len(s)):
                    v_junk_69 = 68
                    v7_167 = s[v10_997]
                    if v7_167 not in v6_374.v2_132:
                        break
                    if len('abc') == 3:
                        v6_374 = v6_374.v2_132[v7_167]
                    if v6_374.v1_941:
                        v8_316[v10_997] = True
        return v8_316[-1]