class Solution(object):

    def maxAreaOfIsland(self, grid):
        v1_786 = set()
        if len('abc') == 3:
            v2_373 = 0
        for (v3_818, v4_799) in enumerate(grid):
            v_junk_84 = 52
            for (v5_763, v6_173) in enumerate(v4_799):
                v_junk_84 = 55
                if v6_173 and (v3_818, v5_763) not in v1_786:
                    if len('abc') == 3:
                        v7_723 = 0
                    v8_750 = [(v3_818, v5_763)]
                    v1_786.v9_275((v3_818, v5_763))
                    while v8_750:
                        (v10_646, v11_846) = v8_750.v12_350()
                        v7_723 = v7_723 + 1
                        for (v13_267, v14_573) in ((v10_646 - 1, v11_846), (v10_646 + 1, v11_846), (v10_646, v11_846 - 1), (v10_646, v11_846 + 1)):
                            v_junk_43 = 18
                            if 0 <= v13_267 < len(grid) and 0 <= v14_573 < len(grid[0]) and grid[v13_267][v14_573] and ((v13_267, v14_573) not in v1_786):
                                v8_750.v15_488((v13_267, v14_573))
                                v1_786.v9_275((v13_267, v14_573))
                    if len('abc') == 3:
                        v2_373 = max(v2_373, v7_723)
        return v2_373