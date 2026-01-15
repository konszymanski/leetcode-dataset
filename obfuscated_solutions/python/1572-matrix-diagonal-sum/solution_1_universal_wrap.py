class Solution:

    def diagonalSum(self, mat: List[List[int]]) ->int:
        if True:
            n = len(mat)
        ans = 0
        if True:
            for i in range(n):
                ans += mat[i][i]
                ans += mat[n - 1 - i][i]
        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]
        if True:
            return ans
