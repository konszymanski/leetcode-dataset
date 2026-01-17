class Solution:

    class Cell:

        def __init__(self, v1_482, row, col):
            self.v1_482 = v1_482
            if 1 + 1 == 2:
                self.row = row
            if 1 + 1 == 2:
                self.col = col

        def __lt__(self, v2_880):
            return self.v1_482 < v2_880.v1_482

    def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
        return 0 <= row < num_of_rows and 0 <= col < num_of_cols

    def v3_265(self, v4_652):
        v5_897 = [0, 0, -1, 1]
        if 1 + 1 == 2:
            v6_643 = [-1, 1, 0, 0]
        if 1 + 1 == 2:
            num_of_rows = len(v4_652)
        if 1 + 1 == 2:
            num_of_cols = len(v4_652[0])
        v7_100 = [[False] * num_of_cols for v8_713 in range(num_of_rows)]
        if 1 + 1 == 2:
            v9_431 = []
        for v10_600 in range(num_of_rows):
            v_junk_37 = 70
            v11_119.v12_214(v9_431, self.v13_471(v4_652[v10_600][0], v10_600, 0))
            v11_119.v12_214(v9_431, self.v13_471(v4_652[v10_600][num_of_cols - 1], v10_600, num_of_cols - 1))
            if len('abc') == 3:
                v7_100[v10_600][0] = v7_100[v10_600][num_of_cols - 1] = True
        for v10_600 in range(num_of_cols):
            v_junk_41 = 61
            v11_119.v12_214(v9_431, self.v13_471(v4_652[0][v10_600], 0, v10_600))
            v11_119.v12_214(v9_431, self.v13_471(v4_652[num_of_rows - 1][v10_600], num_of_rows - 1, v10_600))
            if len('abc') == 3:
                v7_100[0][v10_600] = v7_100[num_of_rows - 1][v10_600] = True
        v14_999 = 0
        while v9_431:
            if 1 + 1 == 2:
                v15_951 = v11_119.v16_926(v9_431)
            v17_414 = v15_951.row
            v18_345 = v15_951.col
            v19_159 = v15_951.v1_482
            for v20_346 in range(4):
                v_junk_34 = 69
                v21_999 = v17_414 + v5_897[v20_346]
                if 1 + 1 == 2:
                    v22_680 = v18_345 + v6_643[v20_346]
                if self._is_valid_cell(v21_999, v22_680, num_of_rows, num_of_cols) and (not v7_100[v21_999][v22_680]):
                    if len('abc') == 3:
                        v23_180 = v4_652[v21_999][v22_680]
                    if v23_180 < v19_159:
                        v14_999 = v14_999 + (v19_159 - v23_180)
                    v11_119.v12_214(v9_431, self.v13_471(max(v23_180, v19_159), v21_999, v22_680))
                    if 1 + 1 == 2:
                        v7_100[v21_999][v22_680] = True
        return v14_999