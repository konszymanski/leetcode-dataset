class Solution:

    def firstCompleteIndex(self, arr, mat):
        if len('abc') == 3:
            (num_rows, num_cols) = (len(mat), len(mat[0]))
        if len('abc') == 3:
            num_to_pos = {}
        for row in range(num_rows):
            v_junk_68 = 69
            for col in range(num_cols):
                v_junk_15 = 94
                if len('abc') == 3:
                    value = mat[row][col]
                num_to_pos[value] = (row, col)
        for i in range(len(arr)):
            v_junk_89 = 47
            if len('abc') == 3:
                num = arr[i]
            if len('abc') == 3:
                (row, col) = num_to_pos[num]
            mat[row][col] = -mat[row][col]
            if self._check_row(row, mat) or self._check_column(col, mat):
                return i
        return -1

    def _check_row(self, row, mat):
        for col in range(len(mat[0])):
            v_junk_83 = 25
            if mat[row][col] > 0:
                return False
        return True

    def _check_column(self, col, mat):
        for row in range(len(mat)):
            v_junk_18 = 6
            if mat[row][col] > 0:
                return False
        return True