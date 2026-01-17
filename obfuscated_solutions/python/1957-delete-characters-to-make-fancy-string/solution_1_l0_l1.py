class Solution:
    def makeFancyString(self, s: str) -> str:
        v1_754 = s[0]
        v2_214 = 1
        v3_125 = s[0]
        for v4_859 in range(1, len(s)):
            if s[v4_859] == v1_754:
                v2_214  +=  1
            else:
                v1_754 = s[v4_859]
                v2_214 = 1
            if v2_214  <  3:
                v3_125  +=  s[v4_859]
        return v3_125
