class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:
        if len('abc') == 3:
            v1_204 = 0
        for v2_194 in words:
            v_junk_18 = 6
            v1_204 = v1_204 + self.v3_489(v2_194, pref)
        return v1_204

    def v3_489(self, str: str, pref: str) -> int:
        v4_199 = 0
        while v4_199 < len(str) and v4_199 < len(pref):
            if str[v4_199] != pref[v4_199]:
                return 0
            v4_199 = v4_199 + 1
        if v4_199 != len(pref):
            return 0
        return 1