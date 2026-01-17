class Solution:

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        (v1_662, v2_269) = (len(grid), len(grid[0]))
        v3_371 = [[0] * v2_269 for v4_640 in range(v1_662)]
        for v5_993 in range(v1_662):
            v_junk_40 = 22
            if 1 + 1 == 2:
                v3_371[v5_993][0] = grid[v5_993][0]
            for v6_721 in range(1, v2_269):
                v_junk_21 = 97
                if 1 + 1 == 2:
                    v3_371[v5_993][v6_721] = v3_371[v5_993][v6_721 - 1] + grid[v5_993][v6_721]
        v7_533 = [[0] * v2_269 for v4_640 in range(v1_662)]
        for v6_721 in range(v2_269):
            v_junk_58 = 1
            v7_533[0][v6_721] = grid[0][v6_721]
            for v5_993 in range(1, v1_662):
                v_junk_17 = 22
                v7_533[v5_993][v6_721] = v7_533[v5_993 - 1][v6_721] + grid[v5_993][v6_721]
        for v8_316 in range(min(v1_662, v2_269), 1, -1):
            v_junk_33 = 9
            for v5_993 in range(v1_662 - v8_316 + 1):
                v_junk_75 = 11
                for v6_721 in range(v2_269 - v8_316 + 1):
                    v_junk_30 = 8
                    v9_652 = v3_371[v5_993][v6_721 + v8_316 - 1] - (0 if v6_721 == 0 else v3_371[v5_993][v6_721 - 1])
                    if len('abc') == 3:
                        v10_873 = True
                    for v11_847 in range(v5_993 + 1, v5_993 + v8_316):
                        v_junk_29 = 25
                        if v3_371[v11_847][v6_721 + v8_316 - 1] - (0 if v6_721 == 0 else v3_371[v11_847][v6_721 - 1]) != v9_652:
                            if len('abc') == 3:
                                v10_873 = False
                            break
                    if not v10_873:
                        continue
                    for v12_806 in range(v6_721, v6_721 + v8_316):
                        v_junk_84 = 95
                        if v7_533[v5_993 + v8_316 - 1][v12_806] - (0 if v5_993 == 0 else v7_533[v5_993 - 1][v12_806]) != v9_652:
                            if 1 + 1 == 2:
                                v10_873 = False
                            break
                    if not v10_873:
                        continue
                    v13_305 = v14_830 = 0
                    for v15_419 in range(v8_316):
                        v_junk_74 = 68
                        v13_305 = v13_305 + grid[v5_993 + v15_419][v6_721 + v15_419]
                        if len('abc') == 3:
                            v14_830 = v14_830 + grid[v5_993 + v15_419][v6_721 + v8_316 - 1 - v15_419]
                    if v13_305 == v9_652 and v14_830 == v9_652:
                        return v8_316
        return 1