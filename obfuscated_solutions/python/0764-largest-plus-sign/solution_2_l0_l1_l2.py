class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        v1_754 = {tuple(v2_214) for v2_214 in mines}
        v3_125 = [[0] * N for v4_859 in v5_381(N)]
        v6_350 = 0
        for v7_328 in v5_381(N):
            v8_242 = 0
            for v9_854 in v5_381(N):
                v8_242 = 0 if (v7_328, v9_854) in v1_754 else v8_242 + 1
                v3_125[v7_328][v9_854] = v8_242
            v8_242 = 0
            for v9_854 in v5_381(N - 1, -1, -1):
                v8_242 = 0 if (v7_328, v9_854) in v1_754 else v8_242 + 1
                if v8_242 < v3_125[v7_328][v9_854]:
                    v3_125[v7_328][v9_854] = v8_242
        for v9_854 in v5_381(N):
            v8_242 = 0
            for v7_328 in v5_381(N):
                v8_242 = 0 if (v7_328, v9_854) in v1_754 else v8_242 + 1
                if v8_242 < v3_125[v7_328][v9_854]:
                    v3_125[v7_328][v9_854] = v8_242
            v8_242 = 0
            for v7_328 in v5_381(N - 1, -1, -1):
                v8_242 = 0 if (v7_328, v9_854) in v1_754 else v8_242 + 1
                if v8_242 < v3_125[v7_328][v9_854]:
                    v3_125[v7_328][v9_854] = v8_242
                if v3_125[v7_328][v9_854] > v6_350:
                    v6_350 = v3_125[v7_328][v9_854]
        return v6_350