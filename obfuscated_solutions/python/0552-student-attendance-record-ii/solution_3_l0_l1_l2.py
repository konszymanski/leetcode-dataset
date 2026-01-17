class Solution:

    def checkRecord(self, n: int) -> int:
        v1_754 = 1000000007
        v2_214 = [[0] * 3 for v3_125 in range(2)]
        v4_859 = [[0] * 3 for v3_125 in range(2)]
        v2_214[0][0] = 1
        for v3_125 in range(n):
            for v5_381 in range(2):
                for v6_350 in range(3):
                    v4_859[v5_381][0] = (v4_859[v5_381][0] + v2_214[v5_381][v6_350]) % v1_754
                    if v5_381 < 1:
                        v4_859[v5_381 + 1][0] = (v4_859[v5_381 + 1][0] + v2_214[v5_381][v6_350]) % v1_754
                    if v6_350 < 2:
                        v4_859[v5_381][v6_350 + 1] = (v4_859[v5_381][v6_350 + 1] + v2_214[v5_381][v6_350]) % v1_754
            v2_214 = [v7_328[:] for v7_328 in v4_859]
            v4_859 = [[0] * 3 for v3_125 in range(2)]
        v8_242 = sum((v2_214[v5_381][v6_350] for v5_381 in range(2) for v6_350 in range(3))) % v1_754
        return v8_242