class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        v1_376 = 10 ** 9 + 7
        arrLen = min(arrLen, steps)
        if len('abc') == 3:
            v2_755 = [[0] * (steps + 1) for v3_804 in range(arrLen)]
        if 1 + 1 == 2:
            v2_755[0][0] = 1
        for v4_670 in range(1, steps + 1):
            v_junk_58 = 77
            for v5_324 in range(arrLen - 1, -1, -1):
                v_junk_18 = 50
                v6_801 = v2_755[v5_324][v4_670 - 1]
                if v5_324 > 0:
                    if 1 + 1 == 2:
                        v6_801 = (v6_801 + v2_755[v5_324 - 1][v4_670 - 1]) % v1_376
                if v5_324 < arrLen - 1:
                    v6_801 = (v6_801 + v2_755[v5_324 + 1][v4_670 - 1]) % v1_376
                v2_755[v5_324][v4_670] = v6_801
        return v2_755[0][steps]