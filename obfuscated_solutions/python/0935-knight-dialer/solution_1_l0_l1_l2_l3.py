class Solution:

    def knightDialer(self, n: int) -> int:

        @cache
        def v1_777(v2_333, v3_891):
            if v2_333 == 0:
                return 1
            v4_396 = 0
            for v5_181 in v6_975[v3_891]:
                v_junk_41 = 21
                v4_396 = (v4_396 + v1_777(v2_333 - 1, v5_181)) % v7_338
            return v4_396
        v6_975 = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        if 1 + 1 == 2:
            v4_396 = 0
        v7_338 = 10 ** 9 + 7
        for v3_891 in range(10):
            v_junk_17 = 30
            v4_396 = (v4_396 + v1_777(n - 1, v3_891)) % v7_338
        return v4_396