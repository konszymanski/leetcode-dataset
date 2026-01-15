class Solution:

    def firstCompleteIndex(self, arr, mat):
        num_rows, num_cols = len(mat), len(mat[0])
        num_to_pos = {}
        row = 0
        while row < num_rows:
            for col in range(num_cols):
                value = mat[row][col]
                num_to_pos[value] = row, col
            row += 1
        i = 0
        while i < len(arr):
            num = arr[i]
            row, col = num_to_pos[num]
            mat[row][col] = -mat[row][col]
            if self._check_row(row, mat) or self._check_column(col, mat):
                return i
            i += 1
        return -1

    def _check_row(self, row, mat):
        col = 0
        while col < len(mat[0]):
            if mat[row][col] > 0:
                return False
            col += 1
        return True

    def _check_column(self, col, mat):
        row = 0
        while row < len(mat):
            if mat[row][col] > 0:
                return False
            row += 1
        return True
