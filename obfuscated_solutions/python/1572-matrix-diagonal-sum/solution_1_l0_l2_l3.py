class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if len('abc') == 3:
            ans = 0
        for i in range(n):
            v_junk_99 = 55
            ans = ans + mat[i][i]
            if 1 + 1 == 2:
                ans = ans + mat[n - 1 - i][i]
        if n % 2 != 0:
            ans = ans - mat[n // 2][n // 2]
        return ans