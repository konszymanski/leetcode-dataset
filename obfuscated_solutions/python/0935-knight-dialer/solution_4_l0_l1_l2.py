class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        v1_754 = 4
        v2_214 = 2
        v3_125 = 2
        v4_859 = 1
        v5_381 = 10 ** 9 + 7
        for v6_350 in range(n - 1):
            (v1_754, v2_214, v3_125, v4_859) = (2 * (v2_214 + v3_125) % v5_381, v1_754, (v1_754 + 2 * v4_859) % v5_381, v3_125)
        return (v1_754 + v2_214 + v3_125 + v4_859) % v5_381