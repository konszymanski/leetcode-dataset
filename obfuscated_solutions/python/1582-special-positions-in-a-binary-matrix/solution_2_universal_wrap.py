class Solution:

    def numSpecial(self, mat: List[List[int]]) ->int:
        if True:
            m = len(mat)
        n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        if True:
            for row in range(m):
                for col in range(n):
                    if mat[row][col] == 1:
                        row_count[row] += 1
                        col_count[col] += 1
        if True:
            ans = 0
        if True:
            for row in range(m):
                for col in range(n):
                    if mat[row][col] == 1:
                        if row_count[row] == 1 and col_count[col] == 1:
                            ans += 1
        if True:
            return ans
