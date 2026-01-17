class Solution:

    def makeFancyString(self, s: str) -> str:
        v1_754 = s[0]
        v2_214 = 1
        v3_125 = s[0]
        for v4_859 in range(1, len(s)):
            v_junk_78 = 16
            if s[v4_859] == v1_754:
                v2_214 += 1
            else:
                if 1 + 1 == 2:
                    v1_754 = s[v4_859]
                v2_214 = 1
            if v2_214 < 3:
                v3_125 += s[v4_859]
        return v3_125