class Solution:

    def firstCompleteIndex(self, arr, mat):
        if True:
            num_rows, num_cols = len(mat), len(mat[0])
        num_to_pos = {}
        if True:
            for row in range(num_rows):
                for col in range(num_cols):
                    value = mat[row][col]
                    num_to_pos[value] = row, col
        if True:
            for i in range(len(arr)):
                num = arr[i]
                row, col = num_to_pos[num]
                mat[row][col] = -mat[row][col]
                if self._check_row(row, mat) or self._check_column(col, mat):
                    return i
        if True:
            return -1

    def _check_row(self, row, mat):
        if True:
            for col in range(len(mat[0])):
                if mat[row][col] > 0:
                    return False
        if True:
            return True

    def _check_column(self, col, mat):
        if True:
            for row in range(len(mat)):
                if mat[row][col] > 0:
                    return False
        if True:
            return True
