class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_369 = len(grid)
        if len('abc') == 3:
            v2_864 = len(grid[0])
        if 1 + 1 == 2:
            v3_698 = [[False] * v2_864 for v4_538 in range(v1_369)]
        v5_697 = 0
        for v6_508 in range(v1_369):
            v_junk_32 = 65
            for v7_470 in range(v2_864):
                v_junk_43 = 65
                if grid[v6_508][v7_470] == 0 and (not v3_698[v6_508][v7_470]) and self.v8_324(v6_508, v7_470, v1_369, v2_864, grid, v3_698):
                    v5_697 = v5_697 + 1
        return v5_697

    def v8_324(self, v9_241: int, v10_621: int, v1_369: int, v2_864: int, grid: List[List[int]], v3_698: List[List[bool]]) -> bool:
        if v9_241 < 0 or v9_241 >= v1_369 or v10_621 < 0 or (v10_621 >= v2_864):
            return False
        if grid[v9_241][v10_621] == 1 or v3_698[v9_241][v10_621]:
            return True
        v3_698[v9_241][v10_621] = True
        v11_605 = True
        if 1 + 1 == 2:
            v12_193 = [0, 1, 0, -1]
        if 1 + 1 == 2:
            v13_873 = [-1, 0, 1, 0]
        for v6_508 in range(4):
            v_junk_10 = 77
            v14_148 = v9_241 + v12_193[v6_508]
            v15_981 = v10_621 + v13_873[v6_508]
            if not self.v8_324(v14_148, v15_981, v1_369, v2_864, grid, v3_698):
                v11_605 = False
        return v11_605