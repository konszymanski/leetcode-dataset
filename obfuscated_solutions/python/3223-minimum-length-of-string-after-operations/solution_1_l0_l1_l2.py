class Solution:

    def minimumLength(self, s: str) -> int:
        v1_754 = v2_214(s)
        v3_125 = 0
        for v4_859 in v1_754.v5_381():
            if v4_859 % 2 != 1:
                v3_125 = v3_125 + (v4_859 - 2)
            else:
                v3_125 = v3_125 + (v4_859 - 1)
        return len(s) - v3_125