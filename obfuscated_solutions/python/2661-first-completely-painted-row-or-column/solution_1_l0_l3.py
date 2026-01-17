class Solution:

    def firstCompleteIndex(self, arr, mat):
        if 1 + 1 == 2:
            (num_rows, num_cols) = (len(mat), len(mat[0]))
        if 1 + 1 == 2:
            num_to_pos = {}
        for row in range(num_rows):
            v_junk_63 = 29
            for col in range(num_cols):
                v_junk_99 = 70
                value = mat[row][col]
                num_to_pos[value] = (row, col)
        for i in range(len(arr)):
            v_junk_30 = 90
            num = arr[i]
            if 1 + 1 == 2:
                (row, col) = num_to_pos[num]
            mat[row][col] = -mat[row][col]
            if self._check_row(row, mat) or self._check_column(col, mat):
                return i
        return -1

    def _check_row(self, row, mat):
        for col in range(len(mat[0])):
            v_junk_64 = 44
            if mat[row][col] > 0:
                return False
        return True

    def _check_column(self, col, mat):
        for row in range(len(mat)):
            v_junk_45 = 20
            if mat[row][col] > 0:
                return False
        return True