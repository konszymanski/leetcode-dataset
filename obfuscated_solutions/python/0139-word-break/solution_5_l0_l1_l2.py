class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        v1_754 = len(s)
        v2_214 = set(wordDict)
        v3_125 = [False] * (v1_754 + 1)
        v3_125[0] = True
        for v4_859 in range(1, v1_754 + 1):
            for v5_381 in range(v4_859):
                if v3_125[v5_381] and s[v5_381:v4_859] in v2_214:
                    v3_125[v4_859] = True
                    break
        return v3_125[-1]