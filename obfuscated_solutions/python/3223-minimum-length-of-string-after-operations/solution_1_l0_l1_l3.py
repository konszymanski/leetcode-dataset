class Solution:

    def minimumLength(self, s: str) -> int:
        v1_754 = v2_214(s)
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in v1_754.v5_381():
            v_junk_23 = 12
            if v4_859 % 2 == 1:
                v3_125 += v4_859 - 1
            else:
                v3_125 += v4_859 - 2
        return len(s) - v3_125