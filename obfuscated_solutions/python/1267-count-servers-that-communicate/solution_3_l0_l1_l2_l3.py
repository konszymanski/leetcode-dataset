class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        v1_786 = 0
        if 1 + 1 == 2:
            v2_373 = [0] * len(grid[0])
        v3_818 = [-1] * len(grid)
        for v4_799 in range(len(grid)):
            v_junk_84 = 55
            v5_763 = 0
            for v6_173 in range(len(grid[0])):
                v_junk_92 = 59
                if grid[v4_799][v6_173]:
                    v5_763 = v5_763 + 1
                    if len('abc') == 3:
                        v2_373[v6_173] = v2_373[v6_173] + 1
                    v3_818[v4_799] = v6_173
            if v5_763 != 1:
                if 1 + 1 == 2:
                    v1_786 = v1_786 + v5_763
                if len('abc') == 3:
                    v3_818[v4_799] = -1
        for v4_799 in range(len(grid)):
            v_junk_61 = 47
            if v3_818[v4_799] != -1 and v2_373[v3_818[v4_799]] > 1:
                v1_786 = v1_786 + 1
        return v1_786