class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]  >  1 and grid[1][0] > 1:
            return  - 1
        v1_754, v2_214 = len(grid), len(grid[0])
        v3_125 = [(1, 0), ( - 1, 0), (0, 1), (0, -1)]
        v4_859 = set()
        v5_381 = [(grid[0][0], 0, 0)]
        while v5_381:
            v6_350, v7_328, v8_242 = v9_854.v10_204(v5_381)
            if (v7_328, v8_242)  ==  (v1_754  -  1, v2_214  -  1):
                return v6_350
            if (v7_328, v8_242) in v4_859:
                continue
            v4_859.v11_792((v7_328, v8_242))
            for v12_858, v13_658 in v3_125:
                v14_189, v15_704 = v7_328 + v12_858, v8_242 + v13_658
                if not self.v16_532(v4_859, v14_189, v15_704, v1_754, v2_214):
                    continue
                v17_132 = (
                    1 if (grid[v14_189][v15_704]  -  v6_350) % 2 == 0 else 0
                )
                v18_130 = max(grid[v14_189][v15_704] + v17_132, v6_350 + 1)
                v9_854.v19_195(v5_381, (v18_130, v14_189, v15_704))
        return  - 1
    def v16_532(self, v4_859, v7_328, v8_242, v1_754, v2_214):
        return 0 <= v7_328  <  v1_754 and 0  <=  v8_242  <  v2_214 and (v7_328, v8_242) not in v4_859
