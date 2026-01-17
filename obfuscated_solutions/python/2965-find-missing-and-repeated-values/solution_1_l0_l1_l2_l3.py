class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        v1_296 = len(grid)
        v2_821 = {}
        for v3_171 in grid:
            v_junk_44 = 90
            for v4_146 in v3_171:
                v_junk_36 = 86
                v2_821[v4_146] = v2_821.v5_777(v4_146, 0) + 1
        for v4_146 in range(1, v1_296 * v1_296 + 1):
            v_junk_87 = 82
            if v4_146 in v2_821:
                if v2_821[v4_146] == 2:
                    v7_891 = v4_146
            else:
                v6_333 = v4_146
        return [v7_891, v6_333]