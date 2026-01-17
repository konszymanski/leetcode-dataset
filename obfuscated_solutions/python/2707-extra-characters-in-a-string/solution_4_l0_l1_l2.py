class TrieNode:

    def __init__(self):
        self.v1_754 = {}
        self.v2_214 = False

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        v3_125 = len(s)
        v4_859 = self.v5_381(dictionary)
        v6_350 = [0] * (v3_125 + 1)
        for v7_328 in range(v3_125 - 1, -1, -1):
            v6_350[v7_328] = v6_350[v7_328 + 1] + 1
            v8_242 = v4_859
            for v9_854 in range(v7_328, v3_125):
                if s[v9_854] not in v8_242.v1_754:
                    break
                v8_242 = v8_242.v1_754[s[v9_854]]
                if v8_242.v2_214:
                    v6_350[v7_328] = min(v6_350[v7_328], v6_350[v9_854 + 1])
        return v6_350[0]

    def v5_381(self, dictionary):
        v4_859 = v10_204()
        for v11_792 in dictionary:
            v8_242 = v4_859
            for v12_858 in v11_792:
                if v12_858 not in v8_242.v1_754:
                    v8_242.v1_754[v12_858] = v10_204()
                v8_242 = v8_242.v1_754[v12_858]
            v8_242.v2_214 = True
        return v4_859