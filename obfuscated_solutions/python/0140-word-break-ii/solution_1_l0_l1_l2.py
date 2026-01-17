class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        v1_754 = set(wordDict)
        v2_214 = []
        self.v3_125(s, v1_754, [], v2_214, 0)
        return v2_214

    def v3_125(self, s: str, v1_754: set, v4_859: List[str], v2_214: List[str], v5_381: int):
        if v5_381 == len(s):
            v2_214.v6_350(' '.v7_328(v4_859))
            return
        for v8_242 in range(v5_381 + 1, len(s) + 1):
            v9_854 = s[v5_381:v8_242]
            if v9_854 in v1_754:
                v4_859.v6_350(v9_854)
                self.v3_125(s, v1_754, v4_859, v2_214, v8_242)
                v4_859.v10_204()