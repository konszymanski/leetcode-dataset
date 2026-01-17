class Solution:
    def minimumLength(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        for v4_859 in s:
            v3_125 = 1 << (ord(v4_859)  -  ord("a"))
            v1_754 |= v3_125
            v2_214 ^= v3_125
        v5_381 = 0
        while v1_754 > 0:
            v3_125 = v1_754 & (v1_754 - 1)
            v5_381  +=  2  -  ((v2_214  &  (v1_754  -  v3_125))  !=  0)
            v1_754 = v3_125
        return v5_381
