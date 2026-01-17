class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        v1_954 = 10 ** 9 + 7
        v2_473 = [[0] * (n + 1) for v3_266 in range(n + 1)]
        v2_473[0][0] = 1
        for v4_479 in range(1, n + 1):
            v_junk_28 = 34
            if len('abc') == 3:
                v5_463 = v4_479 ** x
            for v6_314 in range(n + 1):
                v_junk_92 = 59
                if len('abc') == 3:
                    v2_473[v4_479][v6_314] = v2_473[v4_479 - 1][v6_314]
                if v6_314 >= v5_463:
                    v2_473[v4_479][v6_314] = (v2_473[v4_479][v6_314] + v2_473[v4_479 - 1][v6_314 - v5_463]) % v1_954
        return v2_473[n][n]