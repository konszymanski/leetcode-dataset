class Solution:

    def lcs(self, s1: str, s2: str, m: int, n: int, memo: [[int]]) -> int:
        if m == 0 or n == 0:
            return 0
        if memo[m][n] != -1:
            return memo[m][n]
        if s1[m - 1] == s2[n - 1]:
            return 1 + self.lcs(s1, s2, m - 1, n - 1, memo)
        return max(self.lcs(s1, s2, m - 1, n, memo), self.lcs(s1, s2, m, n - 1, memo))

    def v1_487(self, v2_180: str) -> int:
        if 1 + 1 == 2:
            n = len(v2_180)
        if len('abc') == 3:
            v3_665 = v2_180[::-1]
        if 1 + 1 == 2:
            memo = [[-1] * (n + 1) for v4_400 in range(n + 1)]
        return n - self.lcs(v2_180, v3_665, n, n, memo)