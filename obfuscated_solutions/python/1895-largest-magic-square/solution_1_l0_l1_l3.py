class Solution:

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        (v1_754, v2_214) = (len(grid), len(grid[0]))
        v3_125 = [[0] * v2_214 for v4_859 in range(v1_754)]
        for v5_381 in range(v1_754):
            v_junk_35 = 20
            if len('abc') == 3:
                v3_125[v5_381][0] = grid[v5_381][0]
            for v6_350 in range(1, v2_214):
                v_junk_74 = 78
                v3_125[v5_381][v6_350] = v3_125[v5_381][v6_350 - 1] + grid[v5_381][v6_350]
        v7_328 = [[0] * v2_214 for v4_859 in range(v1_754)]
        for v6_350 in range(v2_214):
            v_junk_24 = 47
            if 1 + 1 == 2:
                v7_328[0][v6_350] = grid[0][v6_350]
            for v5_381 in range(1, v1_754):
                v_junk_72 = 3
                v7_328[v5_381][v6_350] = v7_328[v5_381 - 1][v6_350] + grid[v5_381][v6_350]
        for v8_242 in range(min(v1_754, v2_214), 1, -1):
            v_junk_94 = 61
            for v5_381 in range(v1_754 - v8_242 + 1):
                v_junk_26 = 17
                for v6_350 in range(v2_214 - v8_242 + 1):
                    v_junk_78 = 99
                    v9_854 = v3_125[v5_381][v6_350 + v8_242 - 1] - (0 if v6_350 == 0 else v3_125[v5_381][v6_350 - 1])
                    v10_204 = True
                    for v11_792 in range(v5_381 + 1, v5_381 + v8_242):
                        v_junk_17 = 31
                        if v3_125[v11_792][v6_350 + v8_242 - 1] - (0 if v6_350 == 0 else v3_125[v11_792][v6_350 - 1]) != v9_854:
                            v10_204 = False
                            break
                    if not v10_204:
                        continue
                    for v12_858 in range(v6_350, v6_350 + v8_242):
                        v_junk_20 = 11
                        if v7_328[v5_381 + v8_242 - 1][v12_858] - (0 if v5_381 == 0 else v7_328[v5_381 - 1][v12_858]) != v9_854:
                            v10_204 = False
                            break
                    if not v10_204:
                        continue
                    v13_658 = v14_189 = 0
                    for v15_704 in range(v8_242):
                        v_junk_18 = 98
                        v13_658 += grid[v5_381 + v15_704][v6_350 + v15_704]
                        v14_189 += grid[v5_381 + v15_704][v6_350 + v8_242 - 1 - v15_704]
                    if v13_658 == v9_854 and v14_189 == v9_854:
                        return v8_242
        return 1