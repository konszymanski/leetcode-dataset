class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def v1_754(v2_214):
            if v2_214 < 0:
                return True
            for v3_125 in wordDict:
                v_junk_87 = 4
                if s[v2_214 - len(v3_125) + 1:v2_214 + 1] == v3_125 and v1_754(v2_214 - len(v3_125)):
                    return True
            return False
        return v1_754(len(s) - 1)