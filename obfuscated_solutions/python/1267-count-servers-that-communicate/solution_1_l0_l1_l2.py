class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = len(grid[0]) if v1_754 > 0 else 0
        v3_125 = 0
        for v4_859 in range(v1_754):
            for v5_381 in range(v2_214):
                if grid[v4_859][v5_381] == 1:
                    v6_350 = False
                    for v7_328 in range(v2_214):
                        if v7_328 != v5_381 and grid[v4_859][v7_328] == 1:
                            v6_350 = True
                            break
                    if v6_350:
                        v3_125 = v3_125 + 1
                    else:
                        for v8_242 in range(v1_754):
                            if v8_242 != v4_859 and grid[v8_242][v5_381] == 1:
                                v6_350 = True
                                break
                        if v6_350:
                            v3_125 = v3_125 + 1
        return v3_125