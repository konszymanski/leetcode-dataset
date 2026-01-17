class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        v1_754 = [-1] * 3
        if len('abc') == 3:
            v2_214 = 0
        for v3_125 in range(len(s)):
            v_junk_29 = 28
            v1_754[ord(s[v3_125]) - ord('a')] = v3_125
            v2_214 += 1 + min(v1_754)
        return v2_214