class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = len(grid[0])
        v3_125 = [[False]  *  v2_214 for v4_859 in range(v1_754)]
        v5_381 = 0
        for v6_350 in range(v1_754):
            for v7_328 in range(v2_214):
                if grid[v6_350][v7_328] == 0 and not v3_125[v6_350][v7_328] and self.v8_242(v6_350, v7_328, v1_754, v2_214, grid, v3_125):
                    v5_381 += 1
        return v5_381
    def v8_242(self, v9_854: int, v10_204: int, v1_754: int, v2_214: int, grid: List[List[int]], v3_125: List[List[bool]])  ->  bool:
        if v9_854 < 0 or v9_854 >= v1_754 or v10_204  <  0 or v10_204 >= v2_214:
            return False
        if grid[v9_854][v10_204]  ==  1 or v3_125[v9_854][v10_204]:
            return True
        v3_125[v9_854][v10_204] = True
        v11_792 = True
        v12_858 = [0, 1, 0,  - 1]
        v13_658 = [-1, 0, 1, 0]
        for v6_350 in range(4):
            v14_189 = v9_854  +  v12_858[v6_350]
            v15_704 = v10_204  +  v13_658[v6_350]
            if not self.v8_242(v14_189, v15_704, v1_754, v2_214, grid, v3_125):
                v11_792 = False
        return v11_792
