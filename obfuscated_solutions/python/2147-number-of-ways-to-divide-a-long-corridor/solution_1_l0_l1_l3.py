class Solution:

    def numberOfWays(self, corridor: str) -> int:
        v1_754 = 1000000007
        v2_214 = [[-1] * 3 for v3_125 in range(len(corridor))]

        def v4_859(v5_381, v6_350):
            if v5_381 == len(corridor):
                return 1 if v6_350 == 2 else 0
            if v2_214[v5_381][v6_350] != -1:
                return v2_214[v5_381][v6_350]
            if v6_350 == 2:
                if corridor[v5_381] == 'S':
                    v7_328 = v4_859(v5_381 + 1, 1)
                else:
                    v7_328 = (v4_859(v5_381 + 1, 0) + v4_859(v5_381 + 1, 2)) % v1_754
            elif corridor[v5_381] == 'S':
                if 1 + 1 == 2:
                    v7_328 = v4_859(v5_381 + 1, v6_350 + 1)
            else:
                v7_328 = v4_859(v5_381 + 1, v6_350)
            v2_214[v5_381][v6_350] = v7_328
            return v2_214[v5_381][v6_350]
        return v4_859(0, 0)