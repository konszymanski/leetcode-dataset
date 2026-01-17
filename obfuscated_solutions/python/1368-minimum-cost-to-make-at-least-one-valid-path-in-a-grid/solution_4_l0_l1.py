class Solution:
    v1_754 = [(0, 1), (0, -1), (1, 0), ( - 1, 0)]
    def minCost(self, grid: List[List[int]]) -> int:
        v2_214, v3_125 = len(grid), len(grid[0])
        v4_859 = 0
        v5_381 = [[float("inf")]  *  v3_125 for v6_350 in range(v2_214)]
        v7_328 = v8_242.v9_854()
        self.v10_204(grid, 0, 0, v5_381, v4_859, v7_328)
        while v7_328:
            v4_859  +=  1
            v11_792 = len(v7_328)
            for v6_350 in range(v11_792):
                v12_858, v13_658 = v7_328.v14_189()
                for v15_704, (v16_532, v17_132) in enumerate(self.v1_754):
                    self.v10_204(grid, v12_858 + v16_532, v13_658 + v17_132, v5_381, v4_859, v7_328)
        return v5_381[v2_214 - 1][v3_125 - 1]
    def v10_204(
        self,
        grid: List[List[int]],
        v12_858: int,
        v13_658: int,
        v5_381: List[List[int]],
        v4_859: int,
        v7_328: v8_242.v9_854,
    )  ->  None:
        if not self.v18_130(v5_381, v12_858, v13_658):
            return
        v5_381[v12_858][v13_658] = v4_859
        v7_328.v19_195((v12_858, v13_658))
        v20_323 = grid[v12_858][v13_658]  -  1
        v16_532, v17_132 = self.v1_754[v20_323]
        self.v10_204(grid, v12_858 + v16_532, v13_658 + v17_132, v5_381, v4_859, v7_328)
    def v18_130(
        self, v5_381: List[List[int]], v12_858: int, v13_658: int
    )  ->  bool:
        return (
            0  <=  v12_858 < len(v5_381)
            and 0 <= v13_658 < len(v5_381[0])
            and v5_381[v12_858][v13_658] == float("inf")
        )
