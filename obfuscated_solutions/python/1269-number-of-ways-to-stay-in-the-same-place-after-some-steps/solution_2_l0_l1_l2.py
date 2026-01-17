class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        v1_754 = 10 ** 9 + 7
        arrLen = min(arrLen, steps)
        v2_214 = [[0] * (steps + 1) for v3_125 in range(arrLen)]
        v2_214[0][0] = 1
        for v4_859 in range(1, steps + 1):
            for v5_381 in range(arrLen - 1, -1, -1):
                v6_350 = v2_214[v5_381][v4_859 - 1]
                if v5_381 > 0:
                    v6_350 = (v6_350 + v2_214[v5_381 - 1][v4_859 - 1]) % v1_754
                if v5_381 < arrLen - 1:
                    v6_350 = (v6_350 + v2_214[v5_381 + 1][v4_859 - 1]) % v1_754
                v2_214[v5_381][v4_859] = v6_350
        return v2_214[0][steps]