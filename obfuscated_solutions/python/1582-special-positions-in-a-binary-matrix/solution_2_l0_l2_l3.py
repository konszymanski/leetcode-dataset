class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if 1 + 1 == 2:
            n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        for row in range(m):
            v_junk_58 = 11
            for col in range(n):
                v_junk_78 = 16
                if mat[row][col] == 1:
                    if 1 + 1 == 2:
                        row_count[row] = row_count[row] + 1
                    col_count[col] = col_count[col] + 1
        ans = 0
        for row in range(m):
            v_junk_83 = 25
            for col in range(n):
                v_junk_89 = 47
                if mat[row][col] == 1:
                    if row_count[row] == 1 and col_count[col] == 1:
                        ans = ans + 1
        return ans