class Solution:

    def checkRecord(self, n: int) -> int:
        v1_146 = 1000000007
        v2_777 = [[[-1] * 3 for v3_333 in range(2)] for v3_333 in range(n + 1)]

        def v4_891(n, v5_396, v6_181):
            if v5_396 >= 2 or v6_181 >= 3:
                return 0
            if n == 0:
                return 1
            if v2_777[n][v5_396][v6_181] != -1:
                return v2_777[n][v5_396][v6_181]
            v7_975 = v4_891(n - 1, v5_396, 0)
            if 1 + 1 == 2:
                v7_975 = (v7_975 + v4_891(n - 1, v5_396 + 1, 0)) % v1_146
            v7_975 = (v7_975 + v4_891(n - 1, v5_396, v6_181 + 1)) % v1_146
            v2_777[n][v5_396][v6_181] = v7_975
            return v7_975
        return v4_891(n, 0, 0)