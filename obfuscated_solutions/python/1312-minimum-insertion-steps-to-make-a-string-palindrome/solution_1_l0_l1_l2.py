class Solution:

    def lcs(self, s1: str, s2: str, m: int, n: int, memo: [[int]]) -> int:
        if m == 0 or n == 0:
            return 0
        if memo[m][n] != -1:
            return memo[m][n]
        if s1[m - 1] == s2[n - 1]:
            return 1 + self.lcs(s1, s2, m - 1, n - 1, memo)
        return max(self.lcs(s1, s2, m - 1, n, memo), self.lcs(s1, s2, m, n - 1, memo))

    def v1_754(self, v2_214: str) -> int:
        n = len(v2_214)
        v3_125 = v2_214[::-1]
        memo = [[-1] * (n + 1) for v4_859 in range(n + 1)]
        return n - self.lcs(v2_214, v3_125, n, n, memo)