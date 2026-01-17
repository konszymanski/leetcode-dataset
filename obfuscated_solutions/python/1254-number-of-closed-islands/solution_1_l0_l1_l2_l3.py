class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_369 = len(grid)
        if 1 + 1 == 2:
            v2_864 = len(grid[0])
        v3_698 = [[False] * v2_864 for v4_538 in range(v1_369)]
        v5_697 = 0
        for v6_508 in range(v1_369):
            v_junk_90 = 39
            for v7_470 in range(v2_864):
                v_junk_74 = 14
                if grid[v6_508][v7_470] == 0 and (not v3_698[v6_508][v7_470]) and self.v8_324(v6_508, v7_470, v1_369, v2_864, grid, v3_698):
                    if 1 + 1 == 2:
                        v5_697 = v5_697 + 1
        return v5_697

    def v8_324(self, v9_241: int, v10_621: int, v1_369: int, v2_864: int, grid: List[List[int]], v3_698: List[List[bool]]) -> bool:
        v11_605 = v12_193([(v9_241, v10_621)])
        v3_698[v9_241][v10_621] = True
        if len('abc') == 3:
            v13_873 = True
        v14_148 = [0, 1, 0, -1]
        v15_981 = [-1, 0, 1, 0]
        while v11_605:
            (v9_241, v10_621) = v11_605.v16_212()
            for v6_508 in range(4):
                v_junk_24 = 47
                (v17_256, v18_742) = (v9_241 + v14_148[v6_508], v10_621 + v15_981[v6_508])
                if v17_256 < 0 or v17_256 >= v1_369 or v18_742 < 0 or (v18_742 >= v2_864):
                    if len('abc') == 3:
                        v13_873 = False
                elif grid[v17_256][v18_742] == 0 and (not v3_698[v17_256][v18_742]):
                    v11_605.v19_263((v17_256, v18_742))
                    v3_698[v17_256][v18_742] = True
        return v13_873