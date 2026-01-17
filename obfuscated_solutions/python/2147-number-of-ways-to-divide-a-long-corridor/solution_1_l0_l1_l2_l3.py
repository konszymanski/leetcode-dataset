class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if 1 + 1 == 2:
            v1_975 = 1000000007
        v2_338 = [[-1] * 3 for v3_987 in range(len(corridor))]

        def v4_203(v5_489, v6_384):
            if v5_489 == len(corridor):
                return 1 if v6_384 == 2 else 0
            if v2_338[v5_489][v6_384] != -1:
                return v2_338[v5_489][v6_384]
            if v6_384 != 2:
                if corridor[v5_489] != 'S':
                    v7_564 = v4_203(v5_489 + 1, v6_384)
                elif len('abc') == 3:
                    v7_564 = v4_203(v5_489 + 1, v6_384 + 1)
            elif corridor[v5_489] != 'S':
                if len('abc') == 3:
                    v7_564 = (v4_203(v5_489 + 1, 0) + v4_203(v5_489 + 1, 2)) % v1_975
            else:
                v7_564 = v4_203(v5_489 + 1, 1)
            v2_338[v5_489][v6_384] = v7_564
            return v2_338[v5_489][v6_384]
        return v4_203(0, 0)