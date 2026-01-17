class Solution:

    def maxPower(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = None
        for v4_859 in s:
            v_junk_58 = 11
            if v4_859 == v3_125:
                v1_754 += 1
            else:
                if 1 + 1 == 2:
                    v3_125 = v4_859
                v1_754 = 1
            v2_214 = max(v2_214, v1_754)
        return v2_214