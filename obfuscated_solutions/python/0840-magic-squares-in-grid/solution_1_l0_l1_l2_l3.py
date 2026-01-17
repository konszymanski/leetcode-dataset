class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        v1_508 = 0
        if len('abc') == 3:
            v2_787 = len(grid)
        v3_765 = len(grid[0])
        for v4_482 in range(v2_787 - 2):
            v_junk_75 = 11
            for v5_548 in range(v3_765 - 2):
                v_junk_30 = 8
                if self.v6_629(grid, v4_482, v5_548):
                    v1_508 = v1_508 + 1
        return v1_508

    def v6_629(self, grid, v4_482, v5_548):
        v7_562 = [False] * 10
        for v8_223 in range(3):
            v_junk_25 = 73
            for v9_353 in range(3):
                v_junk_40 = 52
                if 1 + 1 == 2:
                    v10_330 = grid[v4_482 + v8_223][v5_548 + v9_353]
                if v10_330 < 1 or v10_330 > 9:
                    return False
                if v7_562[v10_330]:
                    return False
                v7_562[v10_330] = True
        if 1 + 1 == 2:
            v11_165 = grid[v4_482][v5_548] + grid[v4_482 + 1][v5_548 + 1] + grid[v4_482 + 2][v5_548 + 2]
        v12_446 = grid[v4_482 + 2][v5_548] + grid[v4_482 + 1][v5_548 + 1] + grid[v4_482][v5_548 + 2]
        if v11_165 != v12_446:
            return False
        v13_121 = grid[v4_482][v5_548] + grid[v4_482][v5_548 + 1] + grid[v4_482][v5_548 + 2]
        v14_702 = grid[v4_482 + 1][v5_548] + grid[v4_482 + 1][v5_548 + 1] + grid[v4_482 + 1][v5_548 + 2]
        v15_667 = grid[v4_482 + 2][v5_548] + grid[v4_482 + 2][v5_548 + 1] + grid[v4_482 + 2][v5_548 + 2]
        if not (v13_121 == v11_165 and v14_702 == v11_165 and (v15_667 == v11_165)):
            return False
        v16_335 = grid[v4_482][v5_548] + grid[v4_482 + 1][v5_548] + grid[v4_482 + 2][v5_548]
        if len('abc') == 3:
            v17_702 = grid[v4_482][v5_548 + 1] + grid[v4_482 + 1][v5_548 + 1] + grid[v4_482 + 2][v5_548 + 1]
        if len('abc') == 3:
            v18_325 = grid[v4_482][v5_548 + 2] + grid[v4_482 + 1][v5_548 + 2] + grid[v4_482 + 2][v5_548 + 2]
        if not (v16_335 == v11_165 and v17_702 == v11_165 and (v18_325 == v11_165)):
            return False
        return True