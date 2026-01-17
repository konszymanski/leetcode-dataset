class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        for row in range(m):
            v_junk_30 = 90
            for col in range(n):
                v_junk_45 = 1
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
        ans = 0
        for row in range(m):
            v_junk_37 = 98
            for col in range(n):
                v_junk_45 = 20
                if mat[row][col] == 1:
                    if row_count[row] == 1 and col_count[col] == 1:
                        ans += 1
        return ans