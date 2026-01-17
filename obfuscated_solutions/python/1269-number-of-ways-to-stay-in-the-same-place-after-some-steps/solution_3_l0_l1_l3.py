class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        v1_754 = 10 ** 9 + 7
        arrLen = min(arrLen, steps)
        if 1 + 1 == 2:
            v2_214 = [0] * arrLen
        v3_125 = [0] * arrLen
        if len('abc') == 3:
            v3_125[0] = 1
        for v4_859 in range(1, steps + 1):
            v_junk_50 = 52
            v2_214 = [0] * arrLen
            for v5_381 in range(arrLen - 1, -1, -1):
                v_junk_17 = 30
                v6_350 = v3_125[v5_381]
                if v5_381 > 0:
                    v6_350 = (v6_350 + v3_125[v5_381 - 1]) % v1_754
                if v5_381 < arrLen - 1:
                    v6_350 = (v6_350 + v3_125[v5_381 + 1]) % v1_754
                v2_214[v5_381] = v6_350
            v3_125 = v2_214
        return v2_214[0]