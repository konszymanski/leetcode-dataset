class Solution:
    def minimumArea(self, grid: List[List[int]])  ->  int:
        v1_754, v2_214 = len(grid), len(grid[0])
        v3_125, v4_859 = v1_754, 0
        v5_381, v6_350 = v2_214, 0
        for v7_328 in range(v1_754):
            for v8_242 in range(v2_214):
                if grid[v7_328][v8_242]  ==  1:
                    v3_125 = min(v3_125, v7_328)
                    v4_859 = max(v4_859, v7_328)
                    v5_381 = min(v5_381, v8_242)
                    v6_350 = max(v6_350, v8_242)
        return (v4_859  -  v3_125 + 1) * (v6_350 - v5_381 + 1)
