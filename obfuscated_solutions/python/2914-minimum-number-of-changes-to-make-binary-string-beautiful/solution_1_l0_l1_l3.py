class Solution:

    def minChanges(self, s: str) -> int:
        v1_754 = s[0]
        v2_214 = 0
        v3_125 = 0
        for v4_859 in s:
            v_junk_90 = 80
            if v4_859 == v1_754:
                v2_214 += 1
                continue
            if v2_214 % 2 == 0:
                v2_214 = 1
            else:
                v2_214 = 0
                v3_125 += 1
            v1_754 = v4_859
        return v3_125