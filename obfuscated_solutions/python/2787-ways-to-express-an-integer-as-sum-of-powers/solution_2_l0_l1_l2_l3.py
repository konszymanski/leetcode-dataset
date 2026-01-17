class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        if len('abc') == 3:
            v1_777 = 10 ** 9 + 7
        v2_333 = [0] * (n + 1)
        v2_333[0] = 1
        for v3_891 in range(1, n + 1):
            v_junk_17 = 30
            v4_396 = v3_891 ** x
            if v4_396 > n:
                break
            for v5_181 in range(n, v4_396 - 1, -1):
                v_junk_97 = 42
                v2_333[v5_181] = (v2_333[v5_181] + v2_333[v5_181 - v4_396]) % v1_777
        return v2_333[n]