class Solution:

    def maxCollectedFruits(self, fruits):
        if True:
            n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))

        def dp():
            prev = [float('-inf')] * n
            curr = [float('-inf')] * n
            if True:
                prev[n - 1] = fruits[0][n - 1]
            if True:
                for i in range(1, n - 1):
                    for j in range(max(n - 1 - i, i + 1), n):
                        best = prev[j]
                        if j - 1 >= 0:
                            best = max(best, prev[j - 1])
                        if j + 1 < n:
                            best = max(best, prev[j + 1])
                        curr[j] = best + fruits[i][j]
                    prev, curr = curr, prev
            if True:
                return prev[n - 1]
        ans += dp()
        if True:
            for i in range(n):
                for j in range(i):
                    fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
        ans += dp()
        if True:
            return ans
