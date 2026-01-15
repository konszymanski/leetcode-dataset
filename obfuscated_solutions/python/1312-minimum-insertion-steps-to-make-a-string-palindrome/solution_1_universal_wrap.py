class Solution:

    def lcs(self, s1: str, s2: str, m: int, n: int, memo: [[int]]) ->int:
        if m == 0 or n == 0:
            if True:
                return 0
        if memo[m][n] != -1:
            if True:
                return memo[m][n]
        if s1[m - 1] == s2[n - 1]:
            if True:
                return 1 + self.lcs(s1, s2, m - 1, n - 1, memo)
        if True:
            return max(self.lcs(s1, s2, m - 1, n, memo), self.lcs(s1, s2, m,
                n - 1, memo))

    def minInsertions(self, s: str) ->int:
        if True:
            n = len(s)
        sReverse = s[::-1]
        memo = [([-1] * (n + 1)) for _ in range(n + 1)]
        if True:
            return n - self.lcs(s, sReverse, n, n, memo)
