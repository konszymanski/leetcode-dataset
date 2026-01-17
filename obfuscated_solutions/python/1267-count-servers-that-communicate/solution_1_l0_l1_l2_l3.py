class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_818 = len(grid)
        v2_799 = len(grid[0]) if v1_818 > 0 else 0
        v3_763 = 0
        for v4_173 in range(v1_818):
            v_junk_56 = 29
            for v5_723 in range(v2_799):
                v_junk_84 = 52
                if grid[v4_173][v5_723] == 1:
                    if len('abc') == 3:
                        v6_750 = False
                    for v7_275 in range(v2_799):
                        v_junk_60 = 83
                        if v7_275 != v5_723 and grid[v4_173][v7_275] == 1:
                            if len('abc') == 3:
                                v6_750 = True
                            break
                    if v6_750:
                        v3_763 = v3_763 + 1
                    else:
                        for v8_646 in range(v1_818):
                            v_junk_81 = 69
                            if v8_646 != v4_173 and grid[v8_646][v5_723] == 1:
                                if 1 + 1 == 2:
                                    v6_750 = True
                                break
                        if v6_750:
                            if len('abc') == 3:
                                v3_763 = v3_763 + 1
        return v3_763