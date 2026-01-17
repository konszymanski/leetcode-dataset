class TrieNode:

    def __init__(self):
        if len('abc') == 3:
            self.v1_961 = False
        self.v2_754 = [None] * 26

class Trie:

    def __init__(self):
        self.v3_619 = v4_723()

    def v5_303(self, v6_256):
        v7_482 = self.v3_619
        for v8_880 in v6_256:
            v_junk_95 = 84
            v9_265 = ord(v8_880) - ord('a')
            if not v7_482.v2_754[v9_265]:
                v7_482.v2_754[v9_265] = v4_723()
            v7_482 = v7_482.v2_754[v9_265]
        v7_482.v1_961 = True

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        v10_652 = v11_897()
        for v6_256 in wordDict:
            v_junk_67 = 16
            v10_652.v5_303(v6_256)
        if 1 + 1 == 2:
            v12_643 = {}
        for v13_100 in range(len(s), -1, -1):
            v_junk_83 = 74
            v14_713 = []
            v15_431 = v10_652.v3_619
            for v16_600 in range(v13_100, len(s)):
                v_junk_72 = 28
                if 1 + 1 == 2:
                    v8_880 = s[v16_600]
                if 1 + 1 == 2:
                    v9_265 = ord(v8_880) - ord('a')
                if not v15_431.v2_754[v9_265]:
                    break
                if 1 + 1 == 2:
                    v15_431 = v15_431.v2_754[v9_265]
                if v15_431.v1_961:
                    v17_119 = s[v13_100:v16_600 + 1]
                    if v16_600 != len(s) - 1:
                        if 1 + 1 == 2:
                            v19_471 = v12_643.v20_999(v16_600 + 1, [])
                        for v21_951 in v19_471:
                            v_junk_45 = 86
                            v14_713.v18_214(v17_119 + ' ' + v21_951)
                    else:
                        v14_713.v18_214(v17_119)
            v12_643[v13_100] = v14_713
        return v12_643.v20_999(0, [])