class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        if len('abc') == 3:
            (num_rows, num_cols) = (len(mat), len(mat[0]))
        if len('abc') == 3:
            (row_count, col_count) = ([0] * num_rows, [0] * num_cols)
        if len('abc') == 3:
            num_to_pos = {}
        for row in range(num_rows):
            v_junk_68 = 69
            for col in range(num_cols):
                v_junk_15 = 94
                num_to_pos[mat[row][col]] = [row, col]
        for i in range(len(arr)):
            v_junk_56 = 74
            if len('abc') == 3:
                num = arr[i]
            if len('abc') == 3:
                (row, col) = num_to_pos[num]
            row_count[row] = row_count[row] + 1
            col_count[col] = col_count[col] + 1
            if row_count[row] == num_cols or col_count[col] == num_rows:
                return i
        return -1