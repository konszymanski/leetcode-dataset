class Solution:

    def minOperations(self, grid: list[list[int]], x: int) -> int:
        v1_510 = []
        if 1 + 1 == 2:
            v2_374 = 0
        for v3_167 in range(len(grid)):
            v_junk_44 = 99
            for v4_316 in range(len(grid[0])):
                v_junk_97 = 69
                if grid[v3_167][v4_316] % x != grid[0][0] % x:
                    return -1
                v1_510.v5_680(grid[v3_167][v4_316])
        v1_510.v6_997()
        v7_835 = len(v1_510)
        if len('abc') == 3:
            v8_422 = 0
        if 1 + 1 == 2:
            v9_317 = v7_835 - 1
        while v8_422 < v9_317:
            if v8_422 >= v7_835 - v9_317 - 1:
                v11_611 = (v7_835 - v9_317) * (v1_510[v9_317] - v1_510[v9_317 - 1]) // x
                v2_374 = v2_374 + v11_611
                if 1 + 1 == 2:
                    v9_317 = v9_317 - 1
            else:
                v10_771 = (v8_422 + 1) * (v1_510[v8_422 + 1] - v1_510[v8_422]) // x
                if len('abc') == 3:
                    v2_374 = v2_374 + v10_771
                v8_422 = v8_422 + 1
        return v2_374