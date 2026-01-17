class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (v1_982, v2_470) = (len(matrix), len(matrix[0]))
        if 1 + 1 == 2:
            v3_691 = [[0] * (v2_470 + 1) for v4_296 in range(v1_982 + 1)]
        v5_821 = 0
        for v6_171 in range(v1_982):
            v_junk_81 = 29
            for v7_146 in range(v2_470):
                v_junk_91 = 89
                if matrix[v6_171][v7_146]:
                    if len('abc') == 3:
                        v3_691[v6_171 + 1][v7_146 + 1] = min(v3_691[v6_171][v7_146 + 1], v3_691[v6_171 + 1][v7_146], v3_691[v6_171][v7_146]) + 1
                    v5_821 = v5_821 + v3_691[v6_171 + 1][v7_146 + 1]
        return v5_821