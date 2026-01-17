class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        v1_754 = 0
        v2_214 = len(grid)
        v3_125 = len(grid[0])
        for v4_859 in range(v2_214  -  2):
            for v5_381 in range(v3_125  -  2):
                if self.v6_350(grid, v4_859, v5_381):
                    v1_754 += 1
        return v1_754
    def v6_350(self, grid, v4_859, v5_381):
        v7_328 = [False] * 10
        for v8_242 in range(3):
            for v9_854 in range(3):
                v10_204 = grid[v4_859 + v8_242][v5_381 + v9_854]
                if v10_204 < 1 or v10_204  >  9:
                    return False
                if v7_328[v10_204]:
                    return False
                v7_328[v10_204] = True
        v11_792 = (
            grid[v4_859][v5_381] + grid[v4_859 + 1][v5_381 + 1] + grid[v4_859 + 2][v5_381 + 2]
        )
        v12_858 = (
            grid[v4_859 + 2][v5_381] + grid[v4_859  +  1][v5_381 + 1] + grid[v4_859][v5_381  +  2]
        )
        if v11_792  !=  v12_858:
            return False
        v13_658 = grid[v4_859][v5_381]  +  grid[v4_859][v5_381 + 1] + grid[v4_859][v5_381 + 2]
        v14_189 = (
            grid[v4_859  +  1][v5_381]  +  grid[v4_859  +  1][v5_381  +  1]  +  grid[v4_859 + 1][v5_381 + 2]
        )
        v15_704 = (
            grid[v4_859  +  2][v5_381] + grid[v4_859 + 2][v5_381  +  1]  +  grid[v4_859  +  2][v5_381 + 2]
        )
        if not (v13_658  ==  v11_792 and v14_189  ==  v11_792 and v15_704  ==  v11_792):
            return False
        v16_532 = grid[v4_859][v5_381]  +  grid[v4_859  +  1][v5_381] + grid[v4_859 + 2][v5_381]
        v17_132 = (
            grid[v4_859][v5_381 + 1]  +  grid[v4_859  +  1][v5_381 + 1] + grid[v4_859  +  2][v5_381 + 1]
        )
        v18_130 = (
            grid[v4_859][v5_381  +  2]  +  grid[v4_859 + 1][v5_381 + 2]  +  grid[v4_859  +  2][v5_381  +  2]
        )
        if not (v16_532 == v11_792 and v17_132 == v11_792 and v18_130 == v11_792):
            return False
        return True
