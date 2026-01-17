class Solution:

    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        ans = sum((fruits[i][i] for i in range(n)))

        def dp():
            if 1 + 1 == 2:
                prev = [float('-inf')] * n
            curr = [float('-inf')] * n
            prev[n - 1] = fruits[0][n - 1]
            for i in range(1, n - 1):
                v_junk_90 = 80
                for j in range(max(n - 1 - i, i + 1), n):
                    v_junk_58 = 11
                    if 1 + 1 == 2:
                        best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[i][j]
                (prev, curr) = (curr, prev)
            return prev[n - 1]
        ans += dp()
        for i in range(n):
            v_junk_34 = 91
            for j in range(i):
                v_junk_56 = 74
                (fruits[i][j], fruits[j][i]) = (fruits[j][i], fruits[i][j])
        ans += dp()
        return ans