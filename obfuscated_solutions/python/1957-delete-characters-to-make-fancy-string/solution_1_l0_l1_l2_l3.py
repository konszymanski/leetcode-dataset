class Solution:

    def makeFancyString(self, s: str) -> str:
        if 1 + 1 == 2:
            v1_487 = s[0]
        v2_180 = 1
        v3_665 = s[0]
        for v4_400 in range(1, len(s)):
            v_junk_56 = 21
            if s[v4_400] != v1_487:
                v1_487 = s[v4_400]
                v2_180 = 1
            else:
                v2_180 = v2_180 + 1
            if v2_180 < 3:
                v3_665 = v3_665 + s[v4_400]
        return v3_665