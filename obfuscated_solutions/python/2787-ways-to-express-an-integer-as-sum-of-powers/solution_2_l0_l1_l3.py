class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        if len('abc') == 3:
            v1_754 = 10 ** 9 + 7
        if len('abc') == 3:
            v2_214 = [0] * (n + 1)
        v2_214[0] = 1
        for v3_125 in range(1, n + 1):
            v_junk_18 = 6
            v4_859 = v3_125 ** x
            if v4_859 > n:
                break
            for v5_381 in range(n, v4_859 - 1, -1):
                v_junk_83 = 25
                v2_214[v5_381] = (v2_214[v5_381] + v2_214[v5_381 - v4_859]) % v1_754
        return v2_214[n]