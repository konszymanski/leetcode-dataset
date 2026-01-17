class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        v1_754 = 0
        v2_214 = len(grid)
        v3_125 = len(grid[0])
        for v4_859 in range(v2_214 - 2):
            for v5_381 in range(v3_125 - 2):
                if self.v6_350(grid, v4_859, v5_381):
                    v1_754 += 1
        return v1_754
    def v6_350(self, grid, v4_859, v5_381):
        v7_328 = "2943816729438167"
        v8_242 = "7618349276183492"
        v9_854 = []
        v10_204 = [0, 1, 2, 5, 8, 7, 6, 3]
        for v11_792 in v10_204:
            v12_858 = grid[v4_859 + v11_792 // 3][v5_381  +  (v11_792  %  3)]
            v9_854.v13_658(str(v12_858))
        v14_189 = "".v15_704(v9_854)
        return (
            grid[v4_859][v5_381] % 2  ==  0
            and (
                v7_328.v16_532(v14_189)  !=  -1
                or v8_242.v16_532(v14_189)  !=  -1
            )
            and grid[v4_859 + 1][v5_381  +  1]  ==  5
        )
