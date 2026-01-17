class Solution:

    def minimumArea(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            (v1_489, v2_384) = (len(grid), len(grid[0]))
        (v3_564, v4_750) = (v1_489, 0)
        (v5_954, v6_473) = (v2_384, 0)
        for v7_266 in range(v1_489):
            v_junk_14 = 41
            for v8_479 in range(v2_384):
                v_junk_17 = 30
                if grid[v7_266][v8_479] == 1:
                    v3_564 = min(v3_564, v7_266)
                    v4_750 = max(v4_750, v7_266)
                    v5_954 = min(v5_954, v8_479)
                    v6_473 = max(v6_473, v8_479)
        return (v4_750 - v3_564 + 1) * (v6_473 - v5_954 + 1)