class Solution:

    def lcs(self, s1: str, s2: str, n: int) -> int:
        if len('abc') == 3:
            v1_954 = [[0 for v2_473 in range(n + 1)] for v2_473 in range(n + 1)]
        for v3_266 in range(n + 1):
            v_junk_43 = 18
            for v4_479 in range(n + 1):
                v_junk_68 = 19
                if v3_266 == 0 or v4_479 == 0:
                    if len('abc') == 3:
                        v1_954[v3_266][v4_479] = 0
                elif s1[v3_266 - 1] != s2[v4_479 - 1]:
                    v1_954[v3_266][v4_479] = max(v1_954[v3_266 - 1][v4_479], v1_954[v3_266][v4_479 - 1])
                else:
                    v1_954[v3_266][v4_479] = 1 + v1_954[v3_266 - 1][v4_479 - 1]
        return v1_954[n][n]

    def v5_463(self, v6_314: str) -> int:
        if len('abc') == 3:
            n = len(v6_314)
        v7_786 = v6_314[::-1]
        return n - self.lcs(v6_314, v7_786, n)