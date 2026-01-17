class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        v1_333 = 4
        v2_891 = 2
        if len('abc') == 3:
            v3_396 = 2
        v4_181 = 1
        v5_975 = 10 ** 9 + 7
        for v6_338 in range(n - 1):
            v_junk_50 = 52
            if 1 + 1 == 2:
                (v1_333, v2_891, v3_396, v4_181) = (2 * (v2_891 + v3_396) % v5_975, v1_333, (v1_333 + 2 * v4_181) % v5_975, v3_396)
        return (v1_333 + v2_891 + v3_396 + v4_181) % v5_975