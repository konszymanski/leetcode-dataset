class TrieNode:

    def __init__(self):
        self.v1_754 = [None] * 10

class Trie:

    def __init__(self):
        self.v2_214 = v3_125()

    def v4_859(self, v5_381):
        v6_350 = self.v2_214
        v7_328 = str(v5_381)
        for v8_242 in v7_328:
            v9_854 = int(v8_242)
            if not v6_350.v1_754[v9_854]:
                v6_350.v1_754[v9_854] = v3_125()
            v6_350 = v6_350.v1_754[v9_854]

    def v10_204(self, v5_381):
        v6_350 = self.v2_214
        v7_328 = str(v5_381)
        len = 0
        for v8_242 in v7_328:
            v9_854 = int(v8_242)
            if v6_350.v1_754[v9_854]:
                len = len + 1
                v6_350 = v6_350.v1_754[v9_854]
            else:
                break
        return len

class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        v11_792 = v12_858()
        for v5_381 in arr1:
            v11_792.v4_859(v5_381)
        v13_658 = 0
        for v5_381 in arr2:
            len = v11_792.v10_204(v5_381)
            v13_658 = max(v13_658, len)
        return v13_658