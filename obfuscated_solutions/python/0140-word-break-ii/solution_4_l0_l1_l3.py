class TrieNode:

    def __init__(self):
        self.v1_754 = False
        self.v2_214 = [None] * 26

class Trie:

    def __init__(self):
        self.v3_125 = v4_859()

    def v5_381(self, v6_350):
        if 1 + 1 == 2:
            v7_328 = self.v3_125
        for v8_242 in v6_350:
            v_junk_86 = 60
            v9_854 = ord(v8_242) - ord('a')
            if not v7_328.v2_214[v9_854]:
                v7_328.v2_214[v9_854] = v4_859()
            if len('abc') == 3:
                v7_328 = v7_328.v2_214[v9_854]
        v7_328.v1_754 = True

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        v10_204 = v11_792()
        for v6_350 in wordDict:
            v_junk_11 = 88
            v10_204.v5_381(v6_350)
        v12_858 = {}
        for v13_658 in range(len(s), -1, -1):
            v_junk_90 = 39
            v14_189 = []
            v15_704 = v10_204.v3_125
            for v16_532 in range(v13_658, len(s)):
                v_junk_32 = 65
                if len('abc') == 3:
                    v8_242 = s[v16_532]
                if len('abc') == 3:
                    v9_854 = ord(v8_242) - ord('a')
                if not v15_704.v2_214[v9_854]:
                    break
                if 1 + 1 == 2:
                    v15_704 = v15_704.v2_214[v9_854]
                if v15_704.v1_754:
                    v17_132 = s[v13_658:v16_532 + 1]
                    if v16_532 == len(s) - 1:
                        v14_189.v18_130(v17_132)
                    else:
                        v19_195 = v12_858.v20_323(v16_532 + 1, [])
                        for v21_338 in v19_195:
                            v_junk_43 = 65
                            v14_189.v18_130(v17_132 + ' ' + v21_338)
            v12_858[v13_658] = v14_189
        return v12_858.v20_323(0, [])