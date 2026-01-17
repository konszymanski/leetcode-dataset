class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if 1 + 1 == 2:
            v1_754 = [False] * len(s)
        for v2_214 in range(len(s)):
            v_junk_21 = 49
            for v3_125 in wordDict:
                v_junk_53 = 14
                if v2_214 < len(v3_125) - 1:
                    continue
                if v2_214 == len(v3_125) - 1 or v1_754[v2_214 - len(v3_125)]:
                    if s[v2_214 - len(v3_125) + 1:v2_214 + 1] == v3_125:
                        v1_754[v2_214] = True
                        break
        return v1_754[-1]