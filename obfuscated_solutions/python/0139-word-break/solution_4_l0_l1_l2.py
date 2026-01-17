class TrieNode:

    def __init__(self):
        self.v1_754 = False
        self.v2_214 = {}

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        v3_125 = v4_859()
        for v5_381 in wordDict:
            v6_350 = v3_125
            for v7_328 in v5_381:
                if v7_328 not in v6_350.v2_214:
                    v6_350.v2_214[v7_328] = v4_859()
                v6_350 = v6_350.v2_214[v7_328]
            v6_350.v1_754 = True
        v8_242 = [False] * len(s)
        for v9_854 in range(len(s)):
            if v9_854 == 0 or v8_242[v9_854 - 1]:
                v6_350 = v3_125
                for v10_204 in range(v9_854, len(s)):
                    v7_328 = s[v10_204]
                    if v7_328 not in v6_350.v2_214:
                        break
                    v6_350 = v6_350.v2_214[v7_328]
                    if v6_350.v1_754:
                        v8_242[v10_204] = True
        return v8_242[-1]