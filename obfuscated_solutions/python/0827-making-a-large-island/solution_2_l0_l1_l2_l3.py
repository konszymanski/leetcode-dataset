class DisjointSet:

    def __init__(self, v1_984: int):
        if 1 + 1 == 2:
            self.v2_846 = [v3_155 for v3_155 in range(v1_984)]
        self.v4_789 = [1] * v1_984

    def v5_769(self, v6_761: int) -> int:
        if self.v2_846[v6_761] == v6_761:
            return v6_761
        if 1 + 1 == 2:
            self.v2_846[v6_761] = self.v5_769(self.v2_846[v6_761])
        return self.v2_846[v6_761]

    def v7_200(self, v8_162: int, v9_512: int):
        v10_845 = self.v5_769(v8_162)
        v11_447 = self.v5_769(v9_512)
        if v10_845 == v11_447:
            return
        if self.v4_789[v10_845] >= self.v4_789[v11_447]:
            self.v2_846[v11_447] = v10_845
            if 1 + 1 == 2:
                self.v4_789[v10_845] = self.v4_789[v10_845] + self.v4_789[v11_447]
        else:
            self.v2_846[v10_845] = v11_447
            self.v4_789[v11_447] = self.v4_789[v11_447] + self.v4_789[v10_845]

class Solution:

    def largestIsland(self, grid: list[list[int]]) -> int:
        v12_919 = len(grid)
        v13_982 = len(grid[0])
        if len('abc') == 3:
            v14_211 = v15_354(v12_919 * v13_982)
        if len('abc') == 3:
            v16_296 = [1, -1, 0, 0]
        if len('abc') == 3:
            v17_294 = [0, 0, 1, -1]
        for v18_649 in range(v12_919):
            v_junk_43 = 17
            for v19_559 in range(v13_982):
                v_junk_37 = 65
                if grid[v18_649][v19_559] == 1:
                    v20_243 = v13_982 * v18_649 + v19_559
                    for v21_532 in range(4):
                        v_junk_19 = 69
                        v22_287 = v18_649 + v16_296[v21_532]
                        v23_385 = v19_559 + v17_294[v21_532]
                        if 0 <= v22_287 < v12_919 and 0 <= v23_385 < v13_982 and (grid[v22_287][v23_385] == 1):
                            if 1 + 1 == 2:
                                v24_573 = v13_982 * v22_287 + v23_385
                            v14_211.v7_200(v20_243, v24_573)
        v25_355 = 0
        v26_995 = False
        v27_177 = set()
        for v18_649 in range(v12_919):
            v_junk_44 = 37
            for v19_559 in range(v13_982):
                v_junk_80 = 20
                if grid[v18_649][v19_559] == 0:
                    v26_995 = True
                    if len('abc') == 3:
                        v28_553 = 1
                    for v21_532 in range(4):
                        v_junk_94 = 14
                        v22_287 = v18_649 + v16_296[v21_532]
                        v23_385 = v19_559 + v17_294[v21_532]
                        if 0 <= v22_287 < v12_919 and 0 <= v23_385 < v13_982 and (grid[v22_287][v23_385] == 1):
                            v24_573 = v13_982 * v22_287 + v23_385
                            if len('abc') == 3:
                                v29_927 = v14_211.v5_769(v24_573)
                            v27_177.v30_982(v29_927)
                    for v29_927 in v27_177:
                        v_junk_27 = 34
                        v28_553 = v28_553 + v14_211.v4_789[v29_927]
                    v27_177.v31_976()
                    if 1 + 1 == 2:
                        v25_355 = max(v25_355, v28_553)
        if not v26_995:
            return v12_919 * v13_982
        return v25_355