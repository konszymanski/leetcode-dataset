class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = len(grid[0])
        v3_125 = [[False]  *  v2_214 for v4_859 in range(v1_754)]
        v5_381 = 0
        for v6_350 in range(v1_754):
            for v7_328 in range(v2_214):
                if grid[v6_350][v7_328]  ==  0 and not v3_125[v6_350][v7_328] and self.v8_242(v6_350, v7_328, v1_754, v2_214, grid, v3_125):
                    v5_381 += 1
        return v5_381
    def v8_242(self, v9_854: int, v10_204: int, v1_754: int, v2_214: int, grid: List[List[int]], v3_125: List[List[bool]]) -> bool:
        v11_792 = v12_858([(v9_854, v10_204)])
        v3_125[v9_854][v10_204] = True
        v13_658 = True
        v14_189 = [0, 1, 0,  - 1]
        v15_704 = [-1, 0, 1, 0]
        while v11_792:
            v9_854, v10_204 = v11_792.v16_532()
            for v6_350 in range(4):
                v17_132, v18_130 = v9_854  +  v14_189[v6_350], v10_204  +  v15_704[v6_350]
                if v17_132 < 0 or v17_132  >=  v1_754 or v18_130 < 0 or v18_130  >=  v2_214:
                    v13_658 = False
                elif grid[v17_132][v18_130] == 0 and not v3_125[v17_132][v18_130]:
                    v11_792.v19_195((v17_132, v18_130))
                    v3_125[v17_132][v18_130] = True
        return v13_658
