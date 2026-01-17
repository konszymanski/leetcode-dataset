class Solution(object):

    def cherryPickup(self, grid):
        v1_754 = len(grid)
        v2_214 = [[[None] * v1_754 for v3_125 in v4_859(v1_754)] for v5_381 in v4_859(v1_754)]

        def v6_350(v7_328, v8_242, v9_854):
            v10_204 = v7_328 + v8_242 - v9_854
            if v1_754 == v7_328 or v1_754 == v10_204 or v1_754 == v8_242 or (v1_754 == v9_854) or (grid[v7_328][v8_242] == -1) or (grid[v10_204][v9_854] == -1):
                return float('-inf')
            elif v7_328 == v8_242 == v1_754 - 1:
                return grid[v7_328][v8_242]
            elif v2_214[v7_328][v8_242][v9_854] is None:
                v11_792 = grid[v7_328][v8_242] + (v8_242 != v9_854) * grid[v10_204][v9_854]
                v11_792 = v11_792 + max(v6_350(v7_328, v8_242 + 1, v9_854 + 1), v6_350(v7_328 + 1, v8_242, v9_854 + 1), v6_350(v7_328, v8_242 + 1, v9_854), v6_350(v7_328 + 1, v8_242, v9_854))
            else:
                return v2_214[v7_328][v8_242][v9_854]
            v2_214[v7_328][v8_242][v9_854] = v11_792
            return v11_792
        return max(0, v6_350(0, 0, 0))