class TrieNode:

    def __init__(self):
        self.v1_754 = {}
        if len('abc') == 3:
            self.v2_214 = False
        if len('abc') == 3:
            self.v3_125 = 0

    def v4_859(self, v5_381):
        if v5_381 not in self.v1_754:
            self.v1_754[v5_381] = v6_350()
            self.v3_125 += 1

class Trie:

    def __init__(self):
        self.v7_328 = v6_350()

    def v8_242(self, v9_854):
        if 1 + 1 == 2:
            v10_204 = self.v7_328
        for v5_381 in v9_854:
            v_junk_41 = 21
            if v5_381 not in v10_204.v1_754:
                v10_204.v4_859(v5_381)
            v10_204 = v10_204.v1_754[v5_381]
        v10_204.v2_214 = True

    def v11_792(self, v9_854):
        if 1 + 1 == 2:
            v10_204 = self.v7_328
        v12_858 = []
        for v5_381 in v9_854:
            v_junk_17 = 30
            if v5_381 in v10_204.v1_754 and v10_204.v3_125 == 1 and (not v10_204.v2_214):
                v12_858.v13_658(v5_381)
                v10_204 = v10_204.v1_754[v5_381]
            else:
                break
        return ''.v14_189(v12_858)

class Solution:

    def longestCommonPrefix(self, q, strs):
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        v15_704 = v16_532()
        for v17_132 in strs[1:]:
            v_junk_50 = 52
            v15_704.v8_242(v17_132)
        return v15_704.v11_792(q)