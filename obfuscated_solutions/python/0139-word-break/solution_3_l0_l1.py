class Solution:
    def wordBreak(self, s: str, wordDict: List[str])  ->  bool:
        v1_754 = [False] * len(s)
        for v2_214 in range(len(s)):
            for v3_125 in wordDict:
                if v2_214  <  len(v3_125)  -  1:
                    continue
                if v2_214 == len(v3_125)  -  1 or v1_754[v2_214 - len(v3_125)]:
                    if s[v2_214 - len(v3_125) + 1 : v2_214  +  1] == v3_125:
                        v1_754[v2_214] = True
                        break
        return v1_754[ - 1]
