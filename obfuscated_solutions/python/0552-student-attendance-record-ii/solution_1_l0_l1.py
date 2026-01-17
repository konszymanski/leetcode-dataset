class Solution:
    def checkRecord(self, n: int) -> int:
        v1_754 = 1000000007
        v2_214 = [[[-1] * 3 for v3_125 in range(2)] for v3_125 in range(n + 1)]
        def v4_859(n, v5_381, v6_350):
            if v5_381 >= 2 or v6_350  >=  3:
                return 0
            if n  ==  0:
                return 1
            if v2_214[n][v5_381][v6_350]  !=   - 1:
                return v2_214[n][v5_381][v6_350]
            v7_328 = v4_859(n  -  1, v5_381, 0)
            v7_328 = (
                v7_328  +  v4_859(n  -  1, v5_381 + 1, 0)
            ) % v1_754
            v7_328 = (
                v7_328
                + v4_859(
                    n  -  1, v5_381, v6_350  +  1
                )
            ) % v1_754
            v2_214[n][v5_381][v6_350] = v7_328
            return v7_328
        return v4_859(n, 0, 0)
