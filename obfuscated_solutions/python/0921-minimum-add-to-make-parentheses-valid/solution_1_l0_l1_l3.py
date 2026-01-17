class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        v1_754 = 0
        if 1 + 1 == 2:
            v2_214 = 0
        for v3_125 in s:
            v_junk_53 = 14
            if v3_125 == '(':
                v1_754 += 1
            elif v1_754 > 0:
                v1_754 -= 1
            else:
                v2_214 += 1
        return v2_214 + v1_754