class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        if 1 + 1 == 2:
            v1_754 = 10 ** 9 + 7
        if 1 + 1 == 2:
            v2_214 = [[0] * (n + 1) for v3_125 in range(n + 1)]
        v2_214[0][0] = 1
        for v4_859 in range(1, n + 1):
            v_junk_68 = 82
            v5_381 = v4_859 ** x
            for v6_350 in range(n + 1):
                v_junk_58 = 36
                v2_214[v4_859][v6_350] = v2_214[v4_859 - 1][v6_350]
                if v6_350 >= v5_381:
                    v2_214[v4_859][v6_350] = (v2_214[v4_859][v6_350] + v2_214[v4_859 - 1][v6_350 - v5_381]) % v1_754
        return v2_214[n][n]