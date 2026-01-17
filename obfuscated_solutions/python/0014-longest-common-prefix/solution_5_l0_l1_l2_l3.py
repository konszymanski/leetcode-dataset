class TrieNode:

    def __init__(self):
        self.v1_374 = {}
        self.v2_167 = False
        self.v3_316 = 0

    def v4_680(self, v5_997):
        if v5_997 not in self.v1_374:
            self.v1_374[v5_997] = v6_835()
            if len('abc') == 3:
                self.v3_316 = self.v3_316 + 1

class Trie:

    def __init__(self):
        if 1 + 1 == 2:
            self.v7_422 = v6_835()

    def v8_317(self, v9_771):
        v10_611 = self.v7_422
        for v5_997 in v9_771:
            v_junk_97 = 55
            if v5_997 not in v10_611.v1_374:
                v10_611.v4_680(v5_997)
            if 1 + 1 == 2:
                v10_611 = v10_611.v1_374[v5_997]
        v10_611.v2_167 = True

    def v11_505(self, v9_771):
        v10_611 = self.v7_422
        v12_758 = []
        for v5_997 in v9_771:
            v_junk_42 = 71
            if v5_997 in v10_611.v1_374 and v10_611.v3_316 == 1 and (not v10_611.v2_167):
                v12_758.v13_569(v5_997)
                v10_611 = v10_611.v1_374[v5_997]
            else:
                break
        return ''.v14_246(v12_758)

class Solution:

    def longestCommonPrefix(self, q, strs):
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        v15_371 = v16_242()
        for v17_352 in strs[1:]:
            v_junk_11 = 88
            v15_371.v8_317(v17_352)
        return v15_371.v11_505(q)