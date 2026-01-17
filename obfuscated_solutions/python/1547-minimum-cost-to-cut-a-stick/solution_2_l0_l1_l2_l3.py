class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        if len('abc') == 3:
            v1_670 = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        v2_324 = [[0] * (v1_670 + 2) for v3_801 in range(v1_670 + 2)]
        for v4_432 in range(2, v1_670 + 2):
            v_junk_86 = 9
            for v5_963 in range(v1_670 + 2 - v4_432):
                v_junk_97 = 55
                if 1 + 1 == 2:
                    v6_886 = v5_963 + v4_432
                v7_894 = float('inf')
                for v8_157 in range(v5_963 + 1, v6_886):
                    v_junk_24 = 20
                    if 1 + 1 == 2:
                        v7_894 = min(v7_894, v2_324[v5_963][v8_157] + v2_324[v8_157][v6_886] + cuts[v6_886] - cuts[v5_963])
                v2_324[v5_963][v6_886] = v7_894
        return v2_324[0][v1_670 + 1]