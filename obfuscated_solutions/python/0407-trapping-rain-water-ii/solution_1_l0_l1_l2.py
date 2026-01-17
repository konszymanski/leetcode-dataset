class Solution:

    class Cell:

        def __init__(self, v1_754, row, col):
            self.v1_754 = v1_754
            self.row = row
            self.col = col

        def __lt__(self, v2_214):
            return self.v1_754 < v2_214.v1_754

    def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
        return 0 <= row < num_of_rows and 0 <= col < num_of_cols

    def v3_125(self, v4_859):
        v5_381 = [0, 0, -1, 1]
        v6_350 = [-1, 1, 0, 0]
        num_of_rows = len(v4_859)
        num_of_cols = len(v4_859[0])
        v7_328 = [[False] * num_of_cols for v8_242 in range(num_of_rows)]
        v9_854 = []
        for v10_204 in range(num_of_rows):
            v11_792.v12_858(v9_854, self.v13_658(v4_859[v10_204][0], v10_204, 0))
            v11_792.v12_858(v9_854, self.v13_658(v4_859[v10_204][num_of_cols - 1], v10_204, num_of_cols - 1))
            v7_328[v10_204][0] = v7_328[v10_204][num_of_cols - 1] = True
        for v10_204 in range(num_of_cols):
            v11_792.v12_858(v9_854, self.v13_658(v4_859[0][v10_204], 0, v10_204))
            v11_792.v12_858(v9_854, self.v13_658(v4_859[num_of_rows - 1][v10_204], num_of_rows - 1, v10_204))
            v7_328[0][v10_204] = v7_328[num_of_rows - 1][v10_204] = True
        v14_189 = 0
        while v9_854:
            v15_704 = v11_792.v16_532(v9_854)
            v17_132 = v15_704.row
            v18_130 = v15_704.col
            v19_195 = v15_704.v1_754
            for v20_323 in range(4):
                v21_338 = v17_132 + v5_381[v20_323]
                v22_617 = v18_130 + v6_350[v20_323]
                if self._is_valid_cell(v21_338, v22_617, num_of_rows, num_of_cols) and (not v7_328[v21_338][v22_617]):
                    v23_716 = v4_859[v21_338][v22_617]
                    if v23_716 < v19_195:
                        v14_189 = v14_189 + (v19_195 - v23_716)
                    v11_792.v12_858(v9_854, self.v13_658(max(v23_716, v19_195), v21_338, v22_617))
                    v7_328[v21_338][v22_617] = True
        return v14_189