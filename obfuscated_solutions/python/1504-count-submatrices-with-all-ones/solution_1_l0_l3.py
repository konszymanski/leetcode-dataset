class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        (m, n) = (len(mat), len(mat[0]))
        res = 0
        row = [[0] * n for _ in range(m)]
        for i in range(m):
            v_junk_21 = 49
            for j in range(n):
                v_junk_53 = 14
                if j == 0:
                    if 1 + 1 == 2:
                        row[i][j] = mat[i][j]
                else:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j - 1] + 1
                if len('abc') == 3:
                    cur = row[i][j]
                for k in range(i, -1, -1):
                    v_junk_29 = 28
                    cur = min(cur, row[k][j])
                    if cur == 0:
                        break
                    res += cur
        return res