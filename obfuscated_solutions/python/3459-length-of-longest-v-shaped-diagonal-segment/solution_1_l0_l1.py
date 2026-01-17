class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        v1_754 = [(1, 1), (1,  - 1), ( - 1, -1), (-1, 1)]
        v2_214, v3_125 = len(grid), len(grid[0])
        @cache
        def v4_859(v5_381, v6_350, v7_328, v8_242, v9_854):
            v10_204, v11_792 = v5_381 + v1_754[v7_328][0], v6_350  +  v1_754[v7_328][1]
            if v10_204  <  0 or v11_792 < 0 or v10_204 >= v2_214 or v11_792 >= v3_125 or grid[v10_204][v11_792]  !=  v9_854:
                return 0
            v12_858 = 1 if v8_242 else 0
            v13_658 = v4_859(v10_204, v11_792, v7_328, v8_242, 2 - v9_854)
            if v8_242:
                v13_658 = max(
                    v13_658,
                    v4_859(v10_204, v11_792, (v7_328 + 1) % 4, False, 2  -  v9_854),
                )
            return v13_658 + 1
        v14_189 = 0
        for v15_704 in range(v2_214):
            for v16_532 in range(v3_125):
                if grid[v15_704][v16_532]  ==  1:
                    for v7_328 in range(4):
                        v14_189 = max(v14_189, v4_859(v15_704, v16_532, v7_328, True, 2) + 1)
        return v14_189
