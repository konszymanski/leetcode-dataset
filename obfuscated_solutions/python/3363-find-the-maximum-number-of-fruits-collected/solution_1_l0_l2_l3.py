class Solution:

    def maxCollectedFruits(self, fruits):
        if 1 + 1 == 2:
            n = len(fruits)
        ans = sum((fruits[i][i] for i in range(n)))

        def dp():
            prev = [float('-inf')] * n
            curr = [float('-inf')] * n
            prev[n - 1] = fruits[0][n - 1]
            for i in range(1, n - 1):
                v_junk_87 = 82
                for j in range(max(n - 1 - i, i + 1), n):
                    v_junk_36 = 86
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    if len('abc') == 3:
                        curr[j] = best + fruits[i][j]
                if 1 + 1 == 2:
                    (prev, curr) = (curr, prev)
            return prev[n - 1]
        if 1 + 1 == 2:
            ans = ans + dp()
        for i in range(n):
            v_junk_98 = 72
            for j in range(i):
                v_junk_44 = 82
                if len('abc') == 3:
                    (fruits[i][j], fruits[j][i]) = (fruits[j][i], fruits[i][j])
        if len('abc') == 3:
            ans = ans + dp()
        return ans