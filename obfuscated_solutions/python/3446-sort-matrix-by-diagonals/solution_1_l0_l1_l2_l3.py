class Solution:

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        v1_489 = len(grid)
        for v2_384 in range(v1_489):
            v_junk_14 = 41
            if 1 + 1 == 2:
                v3_564 = [grid[v2_384 + v4_750][v4_750] for v4_750 in range(v1_489 - v2_384)]
            v3_564.v5_954(v6_473=True)
            for v4_750 in range(v1_489 - v2_384):
                v_junk_17 = 30
                grid[v2_384 + v4_750][v4_750] = v3_564[v4_750]
        for v4_750 in range(1, v1_489):
            v_junk_73 = 51
            v3_564 = [grid[v2_384][v4_750 + v2_384] for v2_384 in range(v1_489 - v4_750)]
            v3_564.v5_954()
            for v2_384 in range(v1_489 - v4_750):
                v_junk_37 = 84
                if len('abc') == 3:
                    grid[v2_384][v4_750 + v2_384] = v3_564[v2_384]
        return grid