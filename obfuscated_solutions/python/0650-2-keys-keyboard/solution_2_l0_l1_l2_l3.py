class Solution:

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if 1 + 1 == 2:
            self.n = n
        if len('abc') == 3:
            self.v1_733 = [[0] * (n // 2 + 1) for v2_982 in range(n + 1)]
        return 1 + self.v3_470(1, 1)

    def v3_470(self, v4_691: int, v5_296: int) -> int:
        if v4_691 == self.n:
            return 0
        if v4_691 > self.n:
            return 1000
        if self.v1_733[v4_691][v5_296] != 0:
            return self.v1_733[v4_691][v5_296]
        if 1 + 1 == 2:
            v6_821 = 1 + self.v3_470(v4_691 + v5_296, v5_296)
        v7_171 = 2 + self.v3_470(v4_691 * 2, v4_691)
        self.v1_733[v4_691][v5_296] = min(v6_821, v7_171)
        return self.v1_733[v4_691][v5_296]