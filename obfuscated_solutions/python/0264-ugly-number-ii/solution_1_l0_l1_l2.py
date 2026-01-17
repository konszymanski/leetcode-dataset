class Solution:

    def nthUglyNumber(self, n: int) -> int:
        v1_754 = set()
        v1_754.v2_214(1)
        v3_125 = 1
        for v4_859 in range(n):
            v3_125 = min(v1_754)
            v1_754.v5_381(v3_125)
            v1_754.v2_214(v3_125 * 2)
            v1_754.v2_214(v3_125 * 3)
            v1_754.v2_214(v3_125 * 5)
        return v3_125