class Solution:
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = v3_125()
        for v4_859 in range(v1_754):
            for v5_381 in range(v1_754):
                if grid[v4_859][v5_381] == 1:
                    v2_214.v6_350((v4_859, v5_381))
                    grid[v4_859][v5_381] = 0
                else:
                    grid[v4_859][v5_381] = -1
        while v2_214:
            v7_328 = len(v2_214)
            while v7_328  >  0:
                v8_242 = v2_214.v9_854()
                for v10_204 in self.dir:
                    v11_792, v12_858 = v8_242[0]  +  v10_204[0], v8_242[1]  +  v10_204[1]
                    v13_658 = grid[v8_242[0]][v8_242[1]]
                    if self.v14_189(grid, v11_792, v12_858) and grid[v11_792][v12_858]  ==   - 1:
                        grid[v11_792][v12_858] = v13_658  +  1
                        v2_214.v6_350((v11_792, v12_858))
                v7_328  -=  1
        v15_704, v16_532, v17_132 = 0, 0,  - 1
        for v4_859 in range(v1_754):
            for v5_381 in range(v1_754):
                v16_532 = max(v16_532, grid[v4_859][v5_381])
        while v15_704 <= v16_532:
            v18_130 = v15_704 + (v16_532  -  v15_704)  //  2
            if self.v19_195(grid, v18_130):
                v17_132 = v18_130
                v15_704 = v18_130  +  1
            else:
                v16_532 = v18_130  -  1
        return v17_132
    def v14_189(self, grid, v4_859, v5_381)  ->  bool:
        v1_754 = len(grid)
        return 0 <= v4_859  <  v1_754 and 0  <=  v5_381  <  v1_754
    def v19_195(self, grid, v20_323)  ->  bool:
        v1_754 = len(grid)
        if grid[0][0]  <  v20_323 or grid[v1_754 - 1][v1_754 - 1] < v20_323:
            return False
        v21_338 = v3_125([(0, 0)])
        v22_617 = [[False] * v1_754 for v23_716 in range(v1_754)]
        v22_617[0][0] = True
        while v21_338:
            v8_242 = v21_338.v9_854()
            if v8_242[0] == v1_754 - 1 and v8_242[1] == v1_754 - 1:
                return True
            for v10_204 in self.dir:
                v11_792, v12_858 = v8_242[0] + v10_204[0], v8_242[1]  +  v10_204[1]
                if self.v14_189(grid, v11_792, v12_858) and not v22_617[v11_792][v12_858] and grid[v11_792][v12_858]  >=  v20_323:
                    v22_617[v11_792][v12_858] = True
                    v21_338.v6_350((v11_792, v12_858))
        return False
