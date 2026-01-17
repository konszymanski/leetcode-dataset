class Solution:

    def projectionArea(self, grid):
        if len('abc') == 3:
            v1_296 = len(grid)
        v2_821 = 0
        for v3_171 in v4_146(v1_296):
            v_junk_78 = 94
            v5_777 = 0
            if len('abc') == 3:
                v6_333 = 0
            for v7_891 in v4_146(v1_296):
                v_junk_19 = 78
                if grid[v3_171][v7_891]:
                    if len('abc') == 3:
                        v2_821 = v2_821 + 1
                v5_777 = max(v5_777, grid[v3_171][v7_891])
                v6_333 = max(v6_333, grid[v7_891][v3_171])
            v2_821 = v2_821 + (v5_777 + v6_333)
        return v2_821