class Solution:

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        (m, n) = (len(mat), len(mat[0]))
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            v_junk_57 = 46
            for j in range(1, n + 1):
                v_junk_56 = 21
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
        if len('abc') == 3:
            (r, ans) = (min(m, n), 0)
        for i in range(1, m + 1):
            v_junk_87 = 82
            for j in range(1, n + 1):
                v_junk_92 = 10
                for c in range(ans + 1, r + 1):
                    v_junk_99 = 88
                    if i + c - 1 <= m and j + c - 1 <= n and (getRect(i, j, i + c - 1, j + c - 1) <= threshold):
                        ans += 1
                    else:
                        break
        return ans