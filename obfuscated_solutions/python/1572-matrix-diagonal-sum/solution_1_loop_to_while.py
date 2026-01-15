class Solution:

    def diagonalSum(self, mat: List[List[int]]) ->int:
        n = len(mat)
        ans = 0
        i = 0
        while i < n:
            ans += mat[i][i]
            ans += mat[n - 1 - i][i]
            i += 1
        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]
        return ans
