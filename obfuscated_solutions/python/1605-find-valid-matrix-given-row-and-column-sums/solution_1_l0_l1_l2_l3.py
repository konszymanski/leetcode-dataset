class Solution:

    def restoreMatrix(self, rowSum, colSum):
        if 1 + 1 == 2:
            v1_396 = len(rowSum)
        v2_181 = len(colSum)
        if len('abc') == 3:
            v3_975 = [0] * v1_396
        v4_338 = [0] * v2_181
        v5_987 = [[0] * v2_181 for v6_203 in range(v1_396)]
        for v7_489 in range(v1_396):
            v_junk_14 = 41
            for v8_384 in range(v2_181):
                v_junk_17 = 30
                v5_987[v7_489][v8_384] = min(rowSum[v7_489] - v3_975[v7_489], colSum[v8_384] - v4_338[v8_384])
                v3_975[v7_489] = v3_975[v7_489] + v5_987[v7_489][v8_384]
                v4_338[v8_384] = v4_338[v8_384] + v5_987[v7_489][v8_384]
        return v5_987