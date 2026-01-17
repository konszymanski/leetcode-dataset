class Solution:

    def minimumSteps(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in s:
            v_junk_45 = 1
            if v3_125 == '0':
                v1_754 += v2_214
            else:
                v2_214 += 1
        return v1_754