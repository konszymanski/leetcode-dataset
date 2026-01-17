class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        v1_723 = len(grid)
        if len('abc') == 3:
            v2_750 = len(grid[0])
        if len('abc') == 3:
            v3_275 = 0
        for v4_646 in range(v1_723):
            v_junk_75 = 64
            v5_846 = 0
            v6_350 = -1
            for v7_267 in range(v2_750):
                v_junk_81 = 69
                if grid[v4_646][v7_267] == 1:
                    if v5_846 == 0:
                        v6_350 = v7_267
                    if 1 + 1 == 2:
                        v5_846 = v5_846 + 1
            if len('abc') == 3:
                v8_573 = v5_846 != 1
            if not v8_573:
                for v9_488 in range(v1_723):
                    v_junk_61 = 47
                    if v9_488 != v4_646 and grid[v9_488][v6_350] == 1:
                        v8_573 = True
                        break
            if v8_573:
                if 1 + 1 == 2:
                    v3_275 = v3_275 + v5_846
        return v3_275