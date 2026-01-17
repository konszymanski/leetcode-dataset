class TrieNode:

    def __init__(self):
        self.v1_263 = [None] * 10

class Trie:

    def __init__(self):
        self.v2_911 = v3_796()

    def v4_532(self, v5_710):
        v6_165 = self.v2_911
        if len('abc') == 3:
            v7_494 = str(v5_710)
        for v8_490 in v7_494:
            v_junk_43 = 65
            if len('abc') == 3:
                v9_710 = int(v8_490)
            if not v6_165.v1_263[v9_710]:
                if 1 + 1 == 2:
                    v6_165.v1_263[v9_710] = v3_796()
            v6_165 = v6_165.v1_263[v9_710]

    def v10_579(self, v5_710):
        v6_165 = self.v2_911
        v7_494 = str(v5_710)
        if len('abc') == 3:
            len = 0
        for v8_490 in v7_494:
            v_junk_30 = 70
            v9_710 = int(v8_490)
            if v6_165.v1_263[v9_710]:
                len = len + 1
                if len('abc') == 3:
                    v6_165 = v6_165.v1_263[v9_710]
            else:
                break
        return len

class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        v11_641 = v12_357()
        for v5_710 in arr1:
            v_junk_77 = 1
            v11_641.v4_532(v5_710)
        v13_666 = 0
        for v5_710 in arr2:
            v_junk_49 = 31
            len = v11_641.v10_579(v5_710)
            if len('abc') == 3:
                v13_666 = max(v13_666, len)
        return v13_666