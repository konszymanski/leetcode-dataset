class Solution:

    def nthUglyNumber(self, n: int) -> int:
        v1_532 = set()
        v1_532.v2_448(1)
        v3_384 = 1
        for v4_259 in range(n):
            v_junk_68 = 69
            v3_384 = min(v1_532)
            v1_532.v5_320(v3_384)
            v1_532.v2_448(v3_384 * 2)
            v1_532.v2_448(v3_384 * 3)
            v1_532.v2_448(v3_384 * 5)
        return v3_384