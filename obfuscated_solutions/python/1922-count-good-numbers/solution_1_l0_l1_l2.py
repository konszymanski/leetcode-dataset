class Solution:

    def countGoodNumbers(self, n: int) -> int:
        v1_754 = 10 ** 9 + 7

        def v2_214(v3_125: int, v4_859: int) -> int:
            (v5_381, v6_350) = (1, v3_125)
            while v4_859 > 0:
                if v4_859 % 2 == 1:
                    v5_381 = v5_381 * v6_350 % v1_754
                v6_350 = v6_350 * v6_350 % v1_754
                v4_859 = v4_859 // 2
            return v5_381
        return v2_214(5, (n + 1) // 2) * v2_214(4, n // 2) % v1_754