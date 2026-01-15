class Solution:

    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))

        def dp():
            prev = [float('-inf')] * n
            curr = [float('-inf')] * n
            prev[n - 1] = fruits[0][n - 1]
            i = 1
            while i < n - 1:
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[i][j]
                prev, curr = curr, prev
                i += 1
            return prev[n - 1]
        ans += dp()
        i = 0
        while i < n:
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
            i += 1
        ans += dp()
        return ans
