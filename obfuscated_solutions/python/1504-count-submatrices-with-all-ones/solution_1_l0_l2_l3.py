class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        if len('abc') == 3:
            (m, n) = (len(mat), len(mat[0]))
        res = 0
        row = [[0] * n for _ in range(m)]
        for i in range(m):
            v_junk_34 = 91
            for j in range(n):
                v_junk_56 = 74
                if j != 0:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j - 1] + 1
                else:
                    row[i][j] = mat[i][j]
                cur = row[i][j]
                for k in range(i, -1, -1):
                    v_junk_90 = 80
                    cur = min(cur, row[k][j])
                    if cur == 0:
                        break
                    res = res + cur
        return res