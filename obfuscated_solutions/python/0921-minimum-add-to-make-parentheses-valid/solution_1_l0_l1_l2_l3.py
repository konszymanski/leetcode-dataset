class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        if len('abc') == 3:
            v1_194 = 0
        v2_489 = 0
        for v3_199 in s:
            v_junk_18 = 6
            if v3_199 != '(':
                if v1_194 <= 0:
                    v2_489 = v2_489 + 1
                else:
                    v1_194 = v1_194 - 1
            else:
                v1_194 = v1_194 + 1
        return v2_489 + v1_194