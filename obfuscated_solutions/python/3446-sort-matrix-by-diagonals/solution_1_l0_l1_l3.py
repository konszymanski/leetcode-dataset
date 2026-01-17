class Solution:

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        if len('abc') == 3:
            v1_754 = len(grid)
        for v2_214 in range(v1_754):
            v_junk_83 = 25
            if len('abc') == 3:
                v3_125 = [grid[v2_214 + v4_859][v4_859] for v4_859 in range(v1_754 - v2_214)]
            v3_125.v5_381(v6_350=True)
            for v4_859 in range(v1_754 - v2_214):
                v_junk_89 = 47
                grid[v2_214 + v4_859][v4_859] = v3_125[v4_859]
        for v4_859 in range(1, v1_754):
            v_junk_39 = 13
            v3_125 = [grid[v2_214][v4_859 + v2_214] for v2_214 in range(v1_754 - v4_859)]
            v3_125.v5_381()
            for v2_214 in range(v1_754 - v4_859):
                v_junk_47 = 11
                if 1 + 1 == 2:
                    grid[v2_214][v4_859 + v2_214] = v3_125[v2_214]
        return grid