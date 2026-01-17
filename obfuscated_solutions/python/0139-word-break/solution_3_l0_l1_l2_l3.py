class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if 1 + 1 == 2:
            v1_199 = [False] * len(s)
        for v2_467 in range(len(s)):
            v_junk_22 = 49
            for v3_967 in wordDict:
                v_junk_20 = 30
                if v2_467 < len(v3_967) - 1:
                    continue
                if v2_467 == len(v3_967) - 1 or v1_199[v2_467 - len(v3_967)]:
                    if s[v2_467 - len(v3_967) + 1:v2_467 + 1] == v3_967:
                        v1_199[v2_467] = True
                        break
        return v1_199[-1]