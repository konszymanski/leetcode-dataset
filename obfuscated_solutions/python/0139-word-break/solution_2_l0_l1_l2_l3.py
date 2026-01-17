class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def v1_674(v2_303):
            if v2_303 < 0:
                return True
            for v3_833 in wordDict:
                v_junk_53 = 36
                if s[v2_303 - len(v3_833) + 1:v2_303 + 1] == v3_833 and v1_674(v2_303 - len(v3_833)):
                    return True
            return False
        return v1_674(len(s) - 1)